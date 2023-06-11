# nothing to configure here



##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct
print('Running',os.path.basename(sys.argv[0]),'mod...')

fw =  bytearray(open(sys.argv[1],'rb').read())

if fw[0xA8E4:0xA8E4+4] == b'\x40\xe9\x00\x00':
    print('Increasing mic gain...')
    fw[0xA8E4:0xA8E4+4] = b'\x4f\xe9\x00\x00'
else:
    print('ERROR: Cant find function')


open(sys.argv[1],'wb').write(fw)
