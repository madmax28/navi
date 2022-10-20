#!env python

import sys
import select
import requests

from navi.core import Navi
from navi.config import NaviConfig
from navi.cli import NaviCli

args = NaviCli()

msg = None
if args.message:
    msg = args.message
elif select.select([sys.stdin], [], [], 0)[0]:
    msg = sys.stdin.read()
elif args.media is None:
    sys.stderr.write("No message specified and nothing found standard input\n")
    sys.exit(-1)

config = NaviConfig(args.config_file)
try:
    navi = Navi(
        config.server_host_url,
        config.client_user_id,
        config.client_user_password,
        config.notification_users,
        config.notification_rooms,
        quiet=args.quiet
    )

    if args.media is not None:
        for med in args.media:
            navi.push_media(str(med))

    if msg is not None:
        navi.push_msg(msg)

    navi.shutdown()
except requests.ConnectionError:
    sys.stderr.write("Connection problem\n")
    sys.exit(-1)
