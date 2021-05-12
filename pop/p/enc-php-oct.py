
def enc(s):
    return """eval(implode("",array_map("chr",[{}])))""".format(','.join(['{:03o}'.format(ord(c)) for c in s]))
