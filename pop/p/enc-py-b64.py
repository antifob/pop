
def enc(s):
    return """exec(__import__('base64').b64decode('{}'))""".format(__import__('base64').b64encode(s.encode()).decode())
