import configparser
from collections import namedtuple


class NaviConfig:

    def __init__(self, config_file):
        config = configparser.ConfigParser()
        config.read(config_file)

        self.sanity_check(config)
        self.parse(config)

    def parse(self, config):
        self.server_host_url = config.get("Server", "HostUrl")

        self.client_user_id = config.get("Client", "UserId")
        self.client_user_password = config.get("Client", "UserPassword")

        try:
            self.notification_users = set(config.get("Notification", "Users").split())
        except:
            self.notification_users = set()

        try:
            self.notification_rooms = set(config.get("Notification", "Rooms").split())
        except:
            self.notification_rooms = set()

    def sanity_check(self, config):
        # TODO
        pass
