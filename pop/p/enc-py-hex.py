
def enc(s):
    return """exec(b''.fromhex('{}'))""".format(s.encode().hex())
