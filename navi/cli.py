import os
import sys
from argparse import ArgumentParser, RawDescriptionHelpFormatter

class NaviCli:

    _desc = """\
Navi -- a matrix notification bot."""

    _epilog = """\
Navi sends notifications to matrix users. Messages are given with the '-m'
option. If none is specified, Navi will read the message from standard input.
Its default configuration file is ~/.navi.cfg. Other files can be used with the
'-c' option."""

    def __init__(self):
#        print("this dir is {}".format(__init__.__this_dir))
        self._parse_cli_args()

    @staticmethod
    def _default_config_file():
        return os.path.expanduser("~/.navi.cfg")

    def _parse_cli_args(self):
        parser = ArgumentParser(description=self._desc,
                                epilog=self._epilog,
                                formatter_class=RawDescriptionHelpFormatter)

        prs = parser.add_argument
        prs('-m', default=None, metavar='<message>', dest='message', help='message')
        prs('-c', default=NaviCli._default_config_file(),
                metavar='<config file>', dest='config_file', help='config file\
                (default: ~/.navi.cfg)')
        prs('-q', action='store_true', dest='quiet', help='Stay quiet')

        parser.parse_args(namespace=self)

        # Verify args
        if not (os.path.exists(self.config_file) and os.path.isfile(self.config_file)):
            sys.stderr.write("Config file doesn't exist: {}\n".format(self.config_file))
            sys.exit(-1)
