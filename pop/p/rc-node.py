
USAGE = 'cmd [arg...]'
NARGS = [1, 0]
LANG = 'js'
EXEC = '''
node -e "PAYLOAD"
'''


def tr(s, n):
    return s.replace('\\', '\\\\').replace("'", "\\'")


pl = '''
(()=>{VAR0=process.platform.includes('win');require('child_process').spawn.apply(null,[(VAR0?'cmd':'sh'),[VAR0?'/c':'-c'].concat('ARG1ARGN')])})()
'''
