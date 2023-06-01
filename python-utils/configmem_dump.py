import libuvk5
import sys
import os


# Handle arguments
if len(sys.argv)!=3: print(f'Usage: {os.path.basename(sys.argv[0])} <COMx> <dest_file.bin>') ; exit(1)

arg_port=sys.argv[1]
arg_file=sys.argv[2] 



# Connect and read
with libuvk5.uvk5(arg_port) as radio:
    if radio.connect():
        _=radio.get_fw_version() #mandatory before reading mem
        with open(sys.argv[2],'wb') as f:
            for i in range(0,64):
                x = radio.get_cfg_mem(i*0x80,0x80)
                f.write(x)
                print(f'Reading {i*0x80:04X}...' )