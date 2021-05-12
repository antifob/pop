USAGE = 'cmd'
NARGS = [1, 1]
LANG = 'py'
EXEC = '''
# use an encoded payload with exec()
python -c "PAYLOAD"
'''


def tr(s, n):
    return s.replace('\\', '\\\\').replace("'", "\\'")


pl = '''
import os;os.system('ARG1')
'''
