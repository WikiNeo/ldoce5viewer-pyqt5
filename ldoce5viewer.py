#!/usr/bin/env python3

import sys

from ldoce5viewer import qtgui


if __name__ == '__main__':
    """
    sys.exit([args])
        Exit from Python. This is implemented by raising the SystemExit exception, so cleanup actions specified by 
        finally clauses of try statements are honored, and it is possible to intercept the exit attempt at an outer 
        level.
    """
    sys.exit(qtgui.run(sys.argv))
