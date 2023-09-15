# nothing to configure here
# mod changes frequency range of FM RADIO from 76–108 MHz to 87-108MHz


##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct
print('Running',os.path.basename(sys.argv[0]),'mod...')

fw =  bytearray(open(sys.argv[1],'rb').read())



fw[0xA2E4:0xA2E4+4] = b"\x5F\x0A\x00\x00"  # Reg05 = 0x0A5F    -> SEEK_TH[15:8]; BAND[7:6]; SPACE[5:4]; VOLUME[3:0]
fw[0x64BC:0x64BC+4] = b"\x6C\x20\xC0\x00"  # MOVS R0, #760     -> MOVS R0, #870 - FM LOW LIMIT (0x6C == 870>>3)




open(sys.argv[1],'wb').write(fw)
