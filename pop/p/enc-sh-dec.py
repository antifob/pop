
def enc(s):
    _ = "f(){ printf %b $(printf '\\\\\\\\\\\\%03o' $@); };eval $(echo "
    ps = [str(ord(c)) for c in s]

    r = []
    for i in range(0, len(ps), 512):
        r += [' '.join(ps[i:i + 512])]

    _ += ','.join(r)
    _ += '|tr , "\\n"|grep .|while read x;do f "$x";done|sed "s|.\\(.\\)|\\1|g")'

    return _
