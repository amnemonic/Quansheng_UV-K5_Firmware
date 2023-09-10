# change below sets to new ones, values are in Hz
tx_low_limit  =    18_000_000
tx_high_limit = 1_300_000_000



##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct

TXLOLIM_FW_LOC = 0x1534
TXHILIM_FW_LOC = 0x1538
BLOCKFN_FW_LOC = 0x1836  # CMP R2, #0xCF

print('\n>>> Running',os.path.basename(sys.argv[0]),'mod...')
fw =  bytearray(open(sys.argv[1],'rb').read())


print('Changing TX limit: {} Hz - {} Hz --> {} Hz - {} Hz'.format(
    struct.unpack_from('<I', fw, offset=TXLOLIM_FW_LOC)[0]*10,
    struct.unpack_from('<I', fw, offset=TXHILIM_FW_LOC)[0]*10,
    tx_low_limit,
    tx_high_limit
    ))


fw[TXLOLIM_FW_LOC:TXLOLIM_FW_LOC+4] = struct.pack('<I',tx_low_limit//10) 
fw[TXHILIM_FW_LOC:TXHILIM_FW_LOC+4] = struct.pack('<I',tx_high_limit//10)



print('Patching tx_not_allowed() funtion...')
if fw[BLOCKFN_FW_LOC:BLOCKFN_FW_LOC+2] == b'\xcf\x2a':
    fw[BLOCKFN_FW_LOC:BLOCKFN_FW_LOC+2] = b'\x5d\xe0'
else:
    print('ERROR: Cant find function')





open(sys.argv[1],'wb').write(fw)
print('Done')