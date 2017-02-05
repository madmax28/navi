import sys

from matrix_client.client import MatrixClient
from matrix_client.errors import *

class Navi:
    """
    The Navi API
    """

    def __init__(self, host_url, user_id, password, target_users, quiet=False):
        """ Starts up the bot. Connects to the homeserver and logs in.

        Args:
            base_url: Server url, e.g. https://example.com:8448
            user_id: @user:example.com
            password: p4ssw0rd
            target_users: List of users (@user_id:example.com) to push messages
                to 
        """
        self.quiet = quiet
        self.target_users = target_users
        self.host_url = host_url
        self.user_id = user_id
        self.password = password

        try:
            self.client = MatrixClient(self.host_url)
            self._log("Connecting to {}...".format(self.host_url))
            self.token = self.client.login_with_password(self.user_id, self.password)
        except MatrixRequestError as e:
            Navi._handle_matrix_exception(e)

        self._fetch_rooms()
        self._log("Current rooms:\n\t{}".format("\n\t".join(self.rooms.keys())))

    def shutdown(self):
        """ Stops the bot """
        self.client.logout()
        self._log("Connection closed.")

    def push_msg(self, msg):
        """ Push a message

        Args:
            msg: The message to push
        """
        self._cleanup_rooms()
        self._create_rooms()

        self._log("Pushing message...")
        for r in self.rooms.values(): r.send_text(msg)

    def leave_all_rooms(self):
        """ Leaves all rooms """
        self._log("Leaving all rooms..")
        for r in self.rooms.values(): r.leave()
        self._log("Left {} rooms".format(len(rooms)))

    def _cleanup_rooms(self):
        """ Leaves rooms that no target user is in """
        for room_id in self.rooms.keys():
            room = self.rooms[room_id]
            users = room.get_joined_members().keys()
            if any(u in users for u in self.target_users): continue
            self._log("Leaving room {} (Name: {})".format(room_id, room.name))
            room.leave()
        self._fetch_rooms()

    def _create_rooms(self):
        """ Create rooms for users not found in any current room """
        # Compile list of all users
        if self.rooms:
            current_users = reduce(lambda a, b: a & b, map(lambda r:
                set(r.get_joined_members().keys()), self.rooms.values()))
        else:
            current_users = set()
        missing_users = self.target_users - current_users
        for u in missing_users:
            try:
                self._log("Creating room for user {}...".format(u))
                self.client.create_room(invitees=[u])
            except MatrixRequestError as e:
                Navi._handle_matrix_exception(e)

    def _fetch_rooms(self):
        """ Fetches list of rooms """
        self.rooms = self.client.get_rooms()

    def _log(self, msg):
        if not self.quiet:
            print(msg)

    @staticmethod
    def _handle_matrix_exception(e):
        """ Print exception and quit """
        sys.stderr.write("Server Error {}: {}\n".format(e.code, e.content))
        sys.exit(-1)
