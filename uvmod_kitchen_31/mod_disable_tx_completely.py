# nothing to configure here



##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct
print('Running',os.path.basename(sys.argv[0]),'mod...')

fw =  bytearray(open(sys.argv[1],'rb').read())

if fw[0x1836:0x1836+2] == b'\xcf\x2a':
    print('Disabling TX capability completely!')
    fw[0x1836:0x1836+2] = b'\xf0\xbd'
else:
    print('ERROR: Cant find function')


open(sys.argv[1],'wb').write(fw)
