import sys

if len(sys.argv)!=2: print('ERROR: Need one argument!') ; exit(1)


code = open(sys.argv[1],'rb').read()

pytext = "shellcode = b'"
for i in range(len(code)):
    pytext += "\\x{:02X}".format(code[i])
pytext +="'"

print(pytext)

