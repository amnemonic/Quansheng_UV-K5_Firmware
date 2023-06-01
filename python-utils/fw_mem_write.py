import libuvk5
import sys
import os


# Handle arguments
if len(sys.argv) not in [4,]: print(f'Usage: {os.path.basename(sys.argv[0])} <COMx> <address> <payload>') ; exit(1)

arg_port = sys.argv[1]
arg_addr = int(sys.argv[2],0)
payload  = bytes.fromhex(sys.argv[3])



# Connect and read
with libuvk5.uvk5(arg_port) as radio:
    if radio.connect():
        print(radio.get_fw_version())
        
        buff=radio.set_fw_mem(arg_addr,payload)
        print(buff.hex())
