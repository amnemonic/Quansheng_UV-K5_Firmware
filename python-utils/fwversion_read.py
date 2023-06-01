import libuvk5
import sys
import os


# Handle arguments
if len(sys.argv) not in [2,]: print(f'Usage: {os.path.basename(sys.argv[0])} <COMx>') ; exit(1)

arg_port = sys.argv[1]

# Connect and read
with libuvk5.uvk5(arg_port) as radio:
    if radio.connect():
        print(radio.get_fw_version())
