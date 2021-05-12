
def enc(s):
    return """eval(base64_decode('{}'))""".format(__import__('base64').b64encode(s.encode()).decode())
