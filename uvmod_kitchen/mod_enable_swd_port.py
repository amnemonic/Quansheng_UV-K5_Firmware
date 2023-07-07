# nothing to configure here

# enables SWD port which is normally disabled during Firwmware startup
# thanks for https://github.com/manujedi

##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct
print('Running',os.path.basename(sys.argv[0]),'mod...')

fw =  bytearray(open(sys.argv[1],'rb').read())


fw[0xB924:0xB924+2] = b'\x00\xBF'  if fw[0xB924:0xB924+2] == b'\xC8\x60'  else print('Function not found @0xB924. Wrong FW version or already patched')
fw[0xB9B2:0xB9B2+2] = b'\x00\xBF'  if fw[0xB9B2:0xB9B2+2] == b'\x48\x60'  else print('Function not found @0xB9B2. Wrong FW version or already patched')

if fw[0xB924:0xB924+2] == b'\x00\xBF' and fw[0xB9B2:0xB9B2+2] == b'\x00\xBF': print('SWD port enabled successfully')


open(sys.argv[1],'wb').write(fw)
