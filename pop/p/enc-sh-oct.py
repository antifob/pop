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

def enc(s):
    _ = "f(){ printf %b $(printf '\\\\\\\\\\\\%03o' $@); };eval $(echo "
    _ += ''.join(['{:03o}'.format(ord(c)) for c in s])
    _ += '|sed "s|\\(...\\)|&\\n|g"|grep .|while read x;do f "0$x";done|sed "s|.\\(.\\)|\\1|g")'
    return _
