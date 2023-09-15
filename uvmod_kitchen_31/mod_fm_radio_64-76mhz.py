# nothing to configure here
# mod changes frequency range of FM RADIO from 76–108 MHz to 64-76MHz


##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct
print('Running',os.path.basename(sys.argv[0]),'mod...')

fw =  bytearray(open(sys.argv[1],'rb').read())

fw[0xA364:0xA364+4] = b"\x50\x20\xC0\x00"  # MOVS R0, #760    -> MOVS R0, #640
fw[0xA2E4:0xA2E4+4] = b"\xDF\x0A\x00\x00"  # Reg05 = 0xA5F    -> Reg05 = 0xADF

fw[0x64BC:0x64BC+4] = b"\x50\x20\xC0\x00"  #MOVS R0, #760     -> MOVS R0, #640 - FM LOW LIMIT ( 640 )
fw[0x64C0:0x64C0+2] = b"\x5f\x21"          #MOVS R1, #0x87    -> MOVS R1, #0x5f - FM HIGH LIMIT (0x5f<<3= 760)



open(sys.argv[1],'wb').write(fw)
