#!/usr/bin/python
"""Set AppFlower admin password

Option:
    --pass=     unless provided, will ask interactively

"""

import sys
import getopt
import hashlib

from dialog_wrapper import Dialog
from executil import system

def usage(s=None):
    if s:
        print >> sys.stderr, "Error:", s
    print >> sys.stderr, "Syntax: %s [options]" % sys.argv[0]
    print >> sys.stderr, __doc__
    sys.exit(1)

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'pass='])
    except getopt.GetoptError, e:
        usage(e)

    password = ""
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--pass':
            password = val
        elif opt == '--email':
            email = val

    if not password:
        d = Dialog('TurnKey Linux - First boot configuration')
        password = d.get_password(
            "AppFlower Password",
            "Enter new password for the AppFlower 'admin' account.")

    hash = hashlib.sha1(password).hexdigest()

    config = "/var/www/appflower/plugins/appFlowerStudioPlugin/config/users.yml"
    system("sed -i \"s|password:.*|password: %s|g\" %s" % (hash, config))

if __name__ == "__main__":
    main()

