# This mod allows you to increase the value of the ABR by 2 by 4 or by 8 , remove # at the beginning of the line , according to the value of interest


# multi=int(64) # 
multi=int(128) # (1 corresponds to 2 seconds, 2 corresponds to 4 seconds... up to 5, which corresponds to 10 seconds)
# multi=int(192) # (1 corresponds to 4 seconds, 2 corresponds to 8 seconds... up to 5, which corresponds to 20 seconds)
# multi=int(256) # (1 corresponds to 8 seconds, 2 corresponds to 16 seconds... up to 5, which corresponds to 40 seconds)
##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct
print('Running',os.path.basename(sys.argv[0]),'mod...')

fw =  bytearray(open(sys.argv[1],'rb').read())

if fw[0x59E6] == 0x40 and fw[0x59E7] == 0x00 :
    print('Doubling screen timeout values...')
    fw[0x59E6:0x59E6+4] = struct.pack('<I',multi)
else:
    print('ERROR: Cant find function')


open(sys.argv[1],'wb').write(fw)
