import libuvk5
import sys
import os
import time
import struct

if len(sys.argv)!=2: print(f'Usage: {os.path.basename(sys.argv[0])} <COMx> ') ; exit(1)

arg_port = sys.argv[1]

with libuvk5.uvk5(arg_port) as radio:
    radio.debug=False
    if radio.connect():
        _=radio.get_fw_version() #mandatory
        calib_data = radio.get_cfg_mem(0x1F40,12)
        calib_coef = struct.unpack('<6H',calib_data)[3]
        while True:
            x = radio.get_adc()
            print('{:.4f} V | RAW={}'.format(760*x[0]/calib_coef/100, x[0]))
            time.sleep(0.2)