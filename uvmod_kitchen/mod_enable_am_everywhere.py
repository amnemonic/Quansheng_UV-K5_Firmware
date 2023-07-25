# nothing to configure here
# Giant thanks to Gabi Zafiu for discovering the offsets and required patch for this!


##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct
print('Running',os.path.basename(sys.argv[0]),'mod...')

fw =  bytearray(open(sys.argv[1],'rb').read())

if fw[0x6232:0x6232+1] == b'\x0B' and fw[0x6246:0x6246+1] == b'\x01' and fw[0x624C:0x624C+2] == b'\xB0\x7B':
    print('Enabling AM everywhere...')
    fw[0x6232:0x6232+1] = b'\x0E'
    fw[0x6246:0x6246+1] = b'\x04'
    fw[0x624C:0x624C+2] = b'\x01\xE0'
else:
    print('ERROR: Cant find function')

open(sys.argv[1],'wb').write(fw)
