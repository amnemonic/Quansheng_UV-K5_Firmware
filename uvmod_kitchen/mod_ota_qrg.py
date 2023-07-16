##--------------------- sets new qrg for ota setup transfer ---------------------------------------------------
##--------------------- no warranty by DO7OO ------------------------------------------------------------------
import os,sys,struct
print('Running',os.path.basename(sys.argv[0]),'mod...')

fw =  bytearray(open(sys.argv[1],'rb').read())

if fw[0x5568:0x5568+4] == b'\x04\xa6\x71\x02':
    print('Set new OTA GRQ to 433.6 MHz ...')
    fw[0x5568:0x5568+4] = b'\x00\x9F\x95\x02'
else:
    print('ERROR: Cant find frequency')
    sys.exit(0)

open(sys.argv[1],'wb').write(fw)
