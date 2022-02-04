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

import os


USAGE = 'cmd [arg...]'
NARGS = [1, 0]
LANG = 'c'
EXEC = ''

pl = '''
int main() {
	system("CMD");
}
'''.strip()

def g(_, args, dst, url):
    # payload was not formatted
    cmd = ' '.join([a.replace('\\', '\\\\').replace('"', '\\"') for a in args])
    s = pl.replace('CMD', cmd)

    with open('{}/src.c'.format(dst), 'w') as fp:
        fp.write(s)

    with open('{}/build.sh'.format(dst), 'w') as fp:
        fp.write('\n'.join([
            'cd $(dirname -- "${0}")',
            'gcc -g -Os -static -nostdlib -nostdinc -fno-pie -no-pie -mno-red-zone \\',
            '    -fno-omit-frame-pointer -pg -mnop-mcount \\',
            '    -o src.com.dbg src.c -fuse-ld=bfd -Wl,-T,/usr/src/cosmopolitan/ape.lds \\',
            '    -include /usr/src/cosmopolitan/cosmopolitan.h /usr/src/cosmopolitan/crt.o /usr/src/cosmopolitan/ape.o /usr/src/cosmopolitan/cosmopolitan.a',
            'objcopy -S -O binary src.com.dbg src.com',
        ]))

    os.system('/bin/sh {}/build.sh 2>/dev/null'.format(dst))

    return '\n'.join([url + f for f in ['src.c', 'src.com', 'src.com.dbg', 'build.sh']])
