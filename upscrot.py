#!/usr/bin/env python2

import sys
import subprocess
import StringIO
import gtk
import pynotify
from datetime import datetime

SERVER = 'ich-wars-nicht.ch'
TARGETDIR = '/var/www/danilo/tmp/screenshots/'
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

clipboard = gtk.clipboard_get()
clipboard.set_text(URLROOT + FILE)
clipboard.store()

if pynotify.init('ftpscrot'):
    pynotify.Notification('ftpscrot', 'Screenshot URL was copied to clipboard.').show()
