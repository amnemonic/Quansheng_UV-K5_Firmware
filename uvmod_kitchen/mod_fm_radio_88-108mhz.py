# nothing to configure here
# mod changes frequency range of FM RADIO from 76–108 MHz to 88-108MHz (untested)


##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct
print('Running',os.path.basename(sys.argv[0]),'mod...')

fw =  bytearray(open(sys.argv[1],'rb').read())




fw[0x6452:0x6452+4] = b"\x6e\x20\xC0\x00"  #MOVS R0, #760     -> MOVS R0, #880 - FM LOW LIMIT




open(sys.argv[1],'wb').write(fw)
