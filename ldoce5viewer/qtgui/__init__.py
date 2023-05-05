"""
Entry point for the application
"""

# system level module
from __future__ import unicode_literals, absolute_import, print_function
import sys
import logging
import codecs
import os.path
from optparse import OptionParser

# PyQt5 module
import PyQt5.sip as sip
from PyQt5.QtGui import QIcon
# set a dummy function if QLineEdit doesn't have setPlaceholderText
from PyQt5.QtWidgets import QLineEdit

# project module
from .. import __author__
from .utils.singleapp import SingleApplication
from .utils.error import StdErrWrapper, MyStreamHandler
from .config import get_config
try:
    from . import ui
    from . import resources
except ImportError as e:
    print(e)
    print("need to run '$ make' in order for the program to work")
    exit()

# sip config
sip.setapi('QString', 2)
sip.setapi('QVariant', 2)

# To make sure only one copy of the app is running
_SINGLE_APP_KEY = 'ed437af1-0388-4e13-90e9-486bdc88c77a'

if not hasattr(QLineEdit, 'setPlaceholderText'):
    def _dummy_set_placeholder_text(self, *args, **kwargs):
        pass

    setattr(QLineEdit, 'setPlaceholderText', _dummy_set_placeholder_text)


def _setup_py2exe(config):
    # suspend py2exe's logging facility
    log_path = os.path.join(config._config_dir, 'log.txt')
    try:
        f = codecs.open(log_path, 'w', encoding='utf-8')
    except:
        pass
    else:
        sys.stderr = f


def run(argv):
    """start the application

    This is the entry point for application
    """

    _config = get_config()

    # py2exe - Windows handling
    if sys.platform == 'win32' and (hasattr(sys, 'frozen') or hasattr(sys, 'importers')):
        _setup_py2exe(_config)

    # Parse arguments
    opt_parser = OptionParser()
    opt_parser.set_defaults(debug=False)
    opt_parser.add_option('--debug', action='store_true', help='Enable debug mode')
    (options, args) = opt_parser.parse_args(argv)

    # stderr wrapper
    sys.stderr = StdErrWrapper(sys.stderr)

    # logging
    logger = logging.getLogger()
    handler = MyStreamHandler()
    handler.setFormatter(logging.Formatter('%(levelname)s:%(name)s:%(message)s'))
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG if options.debug else logging.ERROR)

    # Create a single application instance
    app = SingleApplication(argv, _SINGLE_APP_KEY)
    if app.isRunning():
        app.sendMessage('activate')
        return 1

    # Load the configuration file
    _config.debug = options.debug
    _config.load()

    # Set the application's information
    app.setApplicationName(_config.app_name)
    app.setOrganizationName(__author__)
    app.setWindowIcon(QIcon(':/icons/icon.png'))

    # Setup MainWindow
    from .main import MainWindow
    main_window = MainWindow()

    def message_handler(msg):
        if msg == 'activate':
            main_window.activateWindow()
            main_window.setVisible(True)

    app.messageAvailable.connect(message_handler)

    # On Windows-ja
    if app.font().family() == u'MS UI Gothic':
        cand = (('Segoe UI', None), ('Meiryo UI', None), ('Tahoma', 8))
        from PyQt5.QtGui import QFont
        for name, point in cand:
            ps = app.font().pointSize()
            if point is None:
                point = ps if ps != -1 else 9
            font = QFont(name, point)
            if font.exactMatch():
                app.setFont(font)
                break

    # Redirect stderr to the Error Console
    if not options.debug:
        sys.stderr.setApplication(app)

    # Start the application
    r = app.exec_()

    # Quit
    _config.save()

    return r
