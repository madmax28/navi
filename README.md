Navi - A minimal Matrix notification bot
========================================

Navi is a tiny bot for [Matrix][1] that sends notifications to users. It is build upon the [Matrix Python SDK][2].

The motivation behind Navi is to send notifications from anywhere to everywhere. This includes the push services GCM and APNs that [Riot][4] bridges to, without having to rely on services such as Pushbullet or Pushover.

The first time you use it, Navi creates a new room and invites your user to it. The room will be reused afterwards. If you leave the room, so will Navi, and invite you to a new room.

Usage
=====

```Shell
$ navi -q -m "Hey, listen"
$ tail -10 some.log | navi
Connecting to https://matrix.org...
Current rooms:
        !sjgkDaSSBKduHRADCe:matrix.org
Pushing message...
Connection closed.
``` 

Installation
============

1. Initialize the Matrix SDK submodule: `git submodule update --init`
2. Link it into your path (e.g. `ln -s /path/to/navi.py /usr/local/bin/navi`)
3. Set up a matrix account for Navi
4. Create a [configuration][3] in `~/.navi.cfg`:

Dependencies
------------

The Matrix Python SDK requires [requests][5]. Install it with `pip install requests`.
Navi uses filetype. Install it with `pip install filetype`.

[1]: https://matrix.org
[2]: https://github.com/matrix-org/matrix-python-sdk
[3]: ./example.cfg
[4]: https://riot.im
[5]: https://pypi.python.org/pypi/requests
