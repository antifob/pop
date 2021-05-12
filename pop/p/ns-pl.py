USAGE = 'name'
NARGS = [1, 1]
LANG = 'pl'
EXEC = '''
perl -e "PAYLOAD"
'''

pl = '''
gethostbyname('ARG1')
'''
