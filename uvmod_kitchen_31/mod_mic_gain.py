# nothing to configure here



##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct
print('Running',os.path.basename(sys.argv[0]),'mod...')

fw =  bytearray(open(sys.argv[1],'rb').read())

addr1 = 0xA954
addr2 = 0x1D04

if fw[addr1:addr1+4] == b'\x40\xe9\x00\x00' and fw[addr2:addr2+4] == b'\x40\xe9\x00\x00':
    print('Increasing mic gain...')
    fw[addr1:addr1+4] = b'\x4f\xe9\x00\x00'
    fw[addr2:addr2+4] = b'\x4f\xe9\x00\x00'
else:
    print('ERROR: Cant find function')
    sys.exit(0)


open(sys.argv[1],'wb').write(fw)
