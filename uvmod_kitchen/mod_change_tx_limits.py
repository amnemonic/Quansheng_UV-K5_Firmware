# change below sets to new ones, values are in Hz
tx_low_limit  =    18_000_000
tx_high_limit = 1_300_000_000



##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct
print('Running',os.path.basename(sys.argv[0]),'mod...')
fw =  bytearray(open(sys.argv[1],'rb').read())


print('Old tx low limit:  {:>13_} Hz'.format(struct.unpack_from('<I', fw, offset=0x150C)[0]*10))
print('Old tx high limit: {:>13_} Hz'.format(struct.unpack_from('<I', fw, offset=0x1510)[0]*10))


fw[0x150C:0x150C+4] = struct.pack('<I',tx_low_limit//10) 
fw[0x1510:0x1510+4] = struct.pack('<I',tx_high_limit//10)


print('New tx low limit:  {:>13_} Hz'.format(struct.unpack_from('<I', fw, offset=0x150C)[0]*10))
print('New tx high limit: {:>13_} Hz'.format(struct.unpack_from('<I', fw, offset=0x1510)[0]*10))


open(sys.argv[1],'wb').write(fw)
