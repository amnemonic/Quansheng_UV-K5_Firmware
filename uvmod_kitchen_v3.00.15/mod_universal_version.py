#nothing to configure here

##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct
print('\n>>> Running',os.path.basename(sys.argv[0]),'mod...')

fw = bytearray(open(sys.argv[1],'rb').read())

print('Setting universal version...', end=' ')
fw[0x0:0x0+1] = b'*'

open(sys.argv[1],'wb').write(fw)
print('Done')