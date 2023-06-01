import libuvk5
import sys
import os


# Handle arguments
if len(sys.argv) not in [4,5]: print(f'Usage: {os.path.basename(sys.argv[0])} <COMx> <address> <hex_payload>') ; exit(1)

arg_port = sys.argv[1]
arg_addr = int(sys.argv[2],0)
payload  = bytes.fromhex(sys.argv[3])
print('PAYLOAD=',payload.hex())


# Connect and read
with libuvk5.uvk5(arg_port) as radio:
    if radio.connect():
        _=radio.get_fw_version() #mandatory before reading mem
        print(radio.set_cfg_mem(arg_addr,payload).hex())
