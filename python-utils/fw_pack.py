import libuvk5
import sys
import os

if len(sys.argv)!=4: print(f'Usage: {os.path.basename(sys.argv[0])} <decoded_firmware_in.bin> <versionfile_in.bin> <encoded_firmware_out.bin>  ') ; exit(1)


decoded_firmware = open(sys.argv[1],'rb').read()
version_info     = open(sys.argv[2],'rb').read()[0:16]


firmware_with_version = decoded_firmware[0:0x2000] + version_info + decoded_firmware[0x2000:]
encoded_fw = libuvk5.firmware_xor(firmware_with_version)

open(sys.argv[3],'wb').write(encoded_fw+libuvk5.crc16_ccitt_le(encoded_fw))
print(f'Saved encoded firmware to {sys.argv[3]}')
