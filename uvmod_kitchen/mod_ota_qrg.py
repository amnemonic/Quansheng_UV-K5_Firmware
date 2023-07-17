##--------------------- sets new qrg for ota setup transfer ---------------------------------------------------
## Default value for copying setting over the air aka "AIR COPY" is 410.025 MHz
## you can change that default value to some other frequency by changing frequency below

AIR_COPY_FREQ_HZ = 433_600_000

##--------------------- no warranty by DO7OO ------------------------------------------------------------------
import os,sys,struct
print('Running',os.path.basename(sys.argv[0]),'mod...')

fw =  bytearray(open(sys.argv[1],'rb').read())

if fw[0x5568:0x5568+4] == b'\x04\xa6\x71\x02':
    print('Set new OTA GRQ to {:.3f} MHz ...'.format(AIR_COPY_FREQ_HZ/1000/1000))
    fw[0x5568:0x5568+4] = struct.pack('<I',AIR_COPY_FREQ_HZ//10)
else:
    print('ERROR: Cant find frequency')
    sys.exit(0)

open(sys.argv[1],'wb').write(fw)
