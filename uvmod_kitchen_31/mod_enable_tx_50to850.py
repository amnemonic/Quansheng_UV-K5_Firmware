# nothing to configure here



##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct
print('Running',os.path.basename(sys.argv[0]),'mod...')

fw =  bytearray(open(sys.argv[1],'rb').read())

addr = 0x1836

if fw[addr:addr+2] == b'\xcf\x2a':
    print('Disabling TX lock')
    fw[addr:addr+2] = b'\x5d\xe0'
else:
    print('ERROR: Cant find function')


open(sys.argv[1],'wb').write(fw)
