import sys
import struct


fw = open(sys.argv[1],'rb').read()


for i in range(len(fw)//4):
    addr = i*4
    data = struct.unpack('<I',fw[addr:addr+4])[0]
    print('uv_flash_write 0x{:04X} 0x{:08X}'.format(addr,data))


