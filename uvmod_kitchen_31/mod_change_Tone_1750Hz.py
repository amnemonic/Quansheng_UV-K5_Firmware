# If you want, change the frequencies of the tone burst.

tone = int(1750) # change 1750 to any frequency in Hz


##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct
print('Running',os.path.basename(sys.argv[0]),'mod...')

fw =  bytearray(open(sys.argv[1],'rb').read())

if fw[0x2A3C] == 0xd6 and fw[0x2A3C+1] == 0x06 :
    print('Changing tone burst frequency to',tone,'Hz')
    fw[0x2A3C:0x2A3C+4] = struct.pack('<I',tone)
    
else:
    print('ERROR: Cant find function')


open(sys.argv[1],'wb').write(fw)

