import base64


def enc(s):
    _ = 'b(){ openssl base64 -d -A 2>/dev/null||base64 -d||base64 -D; };eval $(echo '
    _ += __import__('base64').b64encode(s.encode()).decode()
    _ += '|b)'
    return _
