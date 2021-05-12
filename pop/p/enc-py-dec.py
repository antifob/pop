
def enc(s):
    return """exec(''.join([chr(VAR0) for VAR0 in [{}]]))""".format(','.join([str(ord(c)) for c in s]))
