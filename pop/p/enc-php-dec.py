
def enc(s):
    return """eval(implode("",array_map("chr",[{}])))""".format(','.join([str(ord(c)) for c in s]))
