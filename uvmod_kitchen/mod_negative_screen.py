# nothing to configure here



##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct
print('Running',os.path.basename(sys.argv[0]),'mod...')

fw =  bytearray(open(sys.argv[1],'rb').read())


if fw[0xB798] == 0xA6:
    print('Enabling negative LCD')
    fw[0xB798] = 0xA7
else:
    print('ERROR: Cant find function')


open(sys.argv[1],'wb').write(fw)
