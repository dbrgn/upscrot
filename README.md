# Upscrot

Upscrot is a simple tool that will take a screenshot using the Linux "scrot"
command and upload it directly to an SSH server.

After uploading, the URL is copied to the X clipboard and can be pasted with
middle click.

## Installing

Install upscrot via pip:

    sudo pip install -U upscrot

## Usage

First run:

1. Run `upscrot.py`. A sample config file will be created.
2. Edit the config file with your server information.

Regular run:

1. Run `upscrot.py`.
2. Draw a rectangle with your mouse around the desired area.
3. Screenshot will be uploaded automatically. The URL will be
   copied to the X clipboard and printed to the console.

It is recommended that you set up key authentication for your SSH server, so
you don't have to type in your password each time.

## Requirements

* python
* python-appdirs
* scrot

## Author

* Danilo Bargen
* https://dbrgn.ch/

## License

Copyright (C) 2011--2016 Danilo Bargen

upscrot is free software: you can redistribute it and/or modify it under the
terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

upscrot is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
upscrot. If not, see http://www.gnu.org/licenses/.
