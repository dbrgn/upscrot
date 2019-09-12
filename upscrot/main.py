#!/usr/bin/env python3

# Directly upload screenshot to sftp server
# Author: Danilo Bargen
# License: GPLv3

import collections
import configparser
import datetime
import os
import subprocess
import sys
import tempfile

import appdirs


def init_config():
    """
    Initialize config.

    If config file exists, read it.
    If not, initialize it.

    """
    confdir = appdirs.user_config_dir('upscrot')
    try:
        os.makedirs(confdir)
    except FileExistsError:
        pass
    confpath = os.path.join(confdir, 'config.ini')

    # Initialize configparser
    config = configparser.ConfigParser(dict_type=collections.OrderedDict)

    # Read config file if it exists
    if os.path.exists(confpath):
        config.read(confpath)
        return config

    # Create it otherwise.
    else:
        config['upload'] = {
            'target_host': 'example.org',
            'target_port': '22',
            'target_dir': '/var/www/tmp/screenshots',
            'base_url': 'https://example.org/tmp/screenshots/',
            'file_prefix': 'screenshot-',
            'file_permissions': '0644',
        }
        with open(confpath, 'w+') as f:
            config.write(f)
        print('Created initial config file.')
        print('Please edit \'%s\' and then run upscrot again.' % confpath)
        sys.exit(1)


def main(config):
    timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
    prefix = config['upload'].get('file_prefix', 'screenshot-')
    screenshot = tempfile.NamedTemporaryFile(
            prefix='%s%s-' % (prefix, timestamp),
            suffix='.png'
    )

    # Take screenshot
    try:
        subprocess.check_call(['scrot', '-s', '-o', screenshot.name])
    except subprocess.CalledProcessError as e:
        print('Could not take screenshot: %s' % e)
        exit(-1)

    # Set permissions
    mode = config['upload'].get('file_permissions', '0644')
    os.chmod(screenshot.name, int(mode, base=8))

    # Upload file
    try:
        subprocess.check_call([
            'scp',
            '-P', config['upload'].get('target_port', '22'),
            screenshot.name,
            '%s:%s' % (config['upload']['target_host'], config['upload']['target_dir']),
        ])
    except subprocess.CalledProcessError as e:
        print('Could not copy file to server: %s' % e)
        exit(-1)
    url = config['upload']['base_url'] + os.path.basename(screenshot.name)

    # X clipboard
    try:
        clipboards = ['-pi', '-bi']
        for clipboard in clipboards:
            xsel = subprocess.Popen(['xsel', clipboard], stdin=subprocess.PIPE)
            xsel.communicate(input=url.encode('utf8'))
    except OSError:
        pass

    print(url)


def entrypoint():
    config = init_config()
    main(config)


if __name__ == '__main__':
    entrypoint()
