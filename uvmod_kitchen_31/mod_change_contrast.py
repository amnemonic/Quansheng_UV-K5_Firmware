# configure contrast in range from 0 to 63. Default value is 31
new_contrast = 31


##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct
print('Running',os.path.basename(sys.argv[0]),'mod...')

fw =  bytearray(open(sys.argv[1],'rb').read())


if fw[0xB820] == 0x1F:
    print(f'Setting new contrast value = {new_contrast & 0x3F}')
    fw[0xB820] = new_contrast & 0x3F
else:
    print('ERROR: Cant find function')


open(sys.argv[1],'wb').write(fw)
