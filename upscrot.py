#!/usr/bin/env python3

# Directly upload screenshot to sftp server
# Author: Danilo Bargen
# License: GPLv3

import subprocess
from datetime import datetime

try:
    import gtk
    import glib
    use_gtk = True
except ImportError:
    use_gtk = False

try:
    import pynotify
    use_pynotify = True
except ImportError:
    use_pynotify = False

SERVER = 'example.org'
TARGETDIR = '/var/www/tmp/screenshots/'
URLROOT = 'http://%s/tmp/screenshots/' % SERVER

TIME = datetime.today().strftime('%Y%m%d_%H%M%S')
FILE = '%s.png' % TIME

try:
    subprocess.check_call(['scrot', '-s', '/tmp/%s' % FILE])
except subprocess.CalledProcessError as e:
    print('Could not take screenshot: %s' % e)
    exit(-1)

try:
    subprocess.check_call(['scp', '/tmp/%s' % FILE, '%s:%s' % (SERVER, TARGETDIR)])
except subprocess.CalledProcessError as e:
    print('Could not copy file to server: %s' % e)
    exit(-1)

# GTK clipboard
if use_gtk:
    try:
        clipboard = gtk.clipboard_get()
        clipboard.set_text(URLROOT + FILE)
        clipboard.store()
        if use_pynotify and pynotify.init('upscrot'):
            pynotify.Notification('upscrot', 'Screenshot URL was copied to clipboard.').show()
    except glib.GError:
        pass

# X clipboard
try:
    clipboards = ['-pi', '-bi']
    for clipboard in clipboards:
        xsel = subprocess.Popen(['xsel', clipboard], stdin=subprocess.PIPE)
        xsel.communicate(input=URLROOT + FILE)
except OSError:
    pass

print('%s%s' % (URLROOT, FILE))
