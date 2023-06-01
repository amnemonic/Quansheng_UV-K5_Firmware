import libuvk5
import sys
import os

if len(sys.argv) not in [2,4]: print(f'Usage: {os.path.basename(sys.argv[0])} <encoded_firmware_in.bin> [<decoded_firmware_out.bin>] [<versionfile_out.bin>] ') ; exit(1)

infile = sys.argv[1]
if len(sys.argv)==4:
    outfw  = sys.argv[2]
    outver = sys.argv[3]
else:
    outfw  = infile.replace('.bin','.dec.bin')
    outver = infile.replace('.bin','.ver.bin')

encoded_firmware =  open(infile,'rb').read()

if libuvk5.crc16_ccitt_le(encoded_firmware[:-2]) == encoded_firmware[-2:]:
    print('CRC OK')
else:
    print('CRC MISMATCH!')

decoded_firmware = libuvk5.firmware_xor(encoded_firmware[:-2])

open(outfw,'wb').write(decoded_firmware[:0x2000]+decoded_firmware[0x2000+16:])
print(f'Saved decoded firmware to {outfw}')

open(outver,'wb').write(decoded_firmware[0x2000:0x2000+16])
print(f'Saved version info to {outver}')


