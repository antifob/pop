
def enc(s):
    _ = "f(){ printf %b $(printf '\\\\\\\\\\\\%03o' $@); };eval $(echo "
    _ += s.encode().hex()
    _ += '|sed "s|\\(..\\)|&\\n|g"|grep .|while read x;do f "0x$x";done|sed "s|.\\(.\\)|\\1|g")'
    return _
