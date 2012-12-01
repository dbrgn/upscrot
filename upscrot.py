#!/usr/bin/env python

# Directly upload screenshot to sftp server
# Author: Danilo Bargen
# License: GPLv3

import sys
import subprocess
import gtk
try:
    import pynotify
except ImportError:
    pass
from datetime import datetime
from glib import GError

SERVER = 'example.org'
TARGETDIR = '/var/www/tmp/screenshots/'
URLROOT = 'http://%s/tmp/screenshots/' % SERVER

TIME = datetime.today().strftime('%Y%m%d_%H%M%S')
FILE = '%s.png' % TIME

try:
    subprocess.check_call(['scrot', '-s', '/tmp/%s' % FILE])
except subprocess.CalledProcessError as e:
    print 'Could not take screenshot: %s' % e
    exit(-1)

try:
    subprocess.check_call(['scp', '/tmp/%s' % FILE, '%s:%s' % (SERVER, TARGETDIR)])
except subprocess.CalledProcessError as e:
    print 'Could not copy file to server: %s' % e
    exit(-1)

try:
    clipboard = gtk.clipboard_get()
    clipboard.set_text(URLROOT + FILE)
    clipboard.store()
    if pynotify.init('upscrot'):
        pynotify.Notification('upscrot', 'Screenshot URL was copied to clipboard.').show()
except (GError, NameError):
    pass
print '%s%s' % (URLROOT, FILE)
