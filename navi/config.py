import ConfigParser
from collections import namedtuple


class NaviConfig:

    def __init__(self, config_file):
        config = ConfigParser.ConfigParser()
        config.read(config_file)

        self.sanity_check(config)
        self.parse(config)

    def parse(self, config):
        self.server_host_url = config.get("Server", "HostUrl")

        self.client_user_id = config.get("Client", "UserId")
        self.client_user_password = config.get("Client", "UserPassword")

        self.notification_users = set(config.get("Notification", "Users").split())

    def sanity_check(self, config):
        # TODO
        pass
