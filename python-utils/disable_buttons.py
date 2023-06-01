import libuvk5
import sys
import os

if len(sys.argv)!=2: print(f'Usage: {os.path.basename(sys.argv[0])} <COMx> ') ; exit(1)

arg_port = sys.argv[1]

with libuvk5.uvk5(arg_port) as radio:
    if radio.connect():
        radio.unk_fn_052F()
