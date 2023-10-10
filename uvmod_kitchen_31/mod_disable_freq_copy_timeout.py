# nothing to configure here

# After applying this mod, the FREQ COPY function ([F]+4) will run indefinetely or if user press [Exit] button

##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct
print('Running',os.path.basename(sys.argv[0]),'mod...')

fw =  bytearray(open(sys.argv[1],'rb').read())


fw[0x4C2C:0x4C2C+2] = b'\x00\xBF'  if fw[0x4C2C:0x4C2C+2] == b'\x52\x1C'  else print('Function not found @0x4C2C. Wrong FW version or already patched')


if fw[0x4C2C:0x4C2C+2] == b'\x00\xBF': print('SCAN FREQ function patched successfully')


open(sys.argv[1],'wb').write(fw)
