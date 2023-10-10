# This mod makes the ABR values actually double (1 corresponds to 2 seconds, 2 corresponds to 4 seconds... up to 5, which corresponds to 10 seconds)
# nothing to configure


##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct
print('Running',os.path.basename(sys.argv[0]),'mod...')

fw =  bytearray(open(sys.argv[1],'rb').read())

if fw[0x59E6] == 0x40:
    print('Doubling screen timeout values...')
    fw[0x59E6] = 0x80
else:
    print('ERROR: Cant find function')


open(sys.argv[1],'wb').write(fw)
