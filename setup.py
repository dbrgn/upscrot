#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(name='upscrot',
      version='0.2',
      author='Danilo Bargen',
      author_email='gezuru@gmail.com',
      url='https://github.com/dbrgn/upscrot/',
      description='A very simple script that will take a screenshot using the linux "scrot" command and upload it directly to a SFTP server.',
      platforms=['Unix'],
      license='GPLv3',
      py_modules=['upscrot'],
      scripts=['upscrot.py'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Natural Language :: English',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python :: 2',
          'Topic :: Desktop Environment :: Gnome',
          'Topic :: Home Automation',
          'Topic :: Utilities',
          ],
     )
