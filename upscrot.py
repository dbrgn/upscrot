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
            'target_dir': '/var/www/tmp/screenshots',
            'base_url': 'https://example.org/tmp/screenshots/',
        }
        with open(confpath, 'w+') as f:
            config.write(f)
        print('Created initial config file.')
        print('Please edit \'%s\' and then run upscrot again.' % confpath)
        sys.exit(1)


def main(config):
    timestamp = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
    filename = '%s.png' % timestamp

    # Take screenshot
    try:
        subprocess.check_call(['scrot', '-s', '/tmp/%s' % filename])
    except subprocess.CalledProcessError as e:
        print('Could not take screenshot: %s' % e)
        exit(-1)

    # Upload file
    try:
        subprocess.check_call([
            'scp',
            '/tmp/%s' % filename,
            '%s:%s' % (config['upload']['target_host'], config['upload']['target_dir']),
        ])
    except subprocess.CalledProcessError as e:
        print('Could not copy file to server: %s' % e)
        exit(-1)
    url = config['upload']['base_url'] + filename

    # X clipboard
    try:
        clipboards = ['-pi', '-bi']
        for clipboard in clipboards:
            xsel = subprocess.Popen(['xsel', clipboard], stdin=subprocess.PIPE)
            xsel.communicate(input=url.encode('utf8'))
    except OSError:
        pass

    print(url)


if __name__ == '__main__':
    config = init_config()
    main(config)
