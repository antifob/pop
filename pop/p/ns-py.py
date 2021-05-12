USAGE = 'name'
NARGS = [1, 1]
LANG = 'py'
EXEC = '''
python -c "PAYLOAD"
'''

pl = '''
__import__('socket').gethostbyname('ARG1')
'''
