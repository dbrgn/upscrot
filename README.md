# Upscrot #

Upscrot is a very simple script that will take a screenshot using the linux "scrot" command and upload it directly to a SFTP server.

## Usage ##

1. Edit the script and change `SERVER`, `TARGETDIR` and `URLROOT` to your likings
2. Execute upscrot script
3. Draw a rectangle with your mouse around the desired area
4. Screenshot will be uploaded automatically. When using Gnome, URL will be copied to clipboard, else it will be printed to the console.

It is recommended that you set up key authentication for your SFTP server, so you don't have to type in your password each time.

## Requirements ##

* Python 2
* Scrot

## Author ##

* Danilo Bargen
* http://ich-wars-nicht.ch/

## License ##

Copyright (C) 2011 Danilo Bargen

upscrot is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

upscrot is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with upscrot. If not, see http://www.gnu.org/licenses/.
