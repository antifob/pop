
def enc(s):
    _ = "f(){ printf %b $(printf '\\\\\\\\\\\\%03o' $@); };eval $(echo "
    _ += ''.join(['{:03o}'.format(ord(c)) for c in s])
    _ += '|sed "s|\\(...\\)|&\\n|g"|grep .|while read x;do f "0$x";done|sed "s|.\\(.\\)|\\1|g")'
    return _
