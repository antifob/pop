
def enc(s):
    return """eval(hex2bin('{}'))""".format(s.encode().hex())
