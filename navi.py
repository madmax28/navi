#!env python2

import sys
import select
import requests

from navi.core import Navi
from navi.config import NaviConfig
from navi.cli import NaviCli

args = NaviCli()

if args.message:
    msg = args.message
elif select.select([sys.stdin], [], [], 0)[0]:
    msg = sys.stdin.read()
else:
    sys.stderr.write("No message specified and nothing found standard input\n")
    sys.exit(-1)

config = NaviConfig(args.config_file)
try:
    navi = Navi(config.server_host_url,
            config.client_user_id,
            config.client_user_password,
            config.notification_users,
            quiet=args.quiet)
    navi.push_msg(msg)
    navi.shutdown()
except requests.ConnectionError:
    sys.stderr.write("Connection problem\n")
    sys.exit(-1)
