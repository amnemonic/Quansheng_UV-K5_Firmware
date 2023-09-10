# nothing to configure here
# Giant thanks to Gabi Zafiu for discovering the offsets and required patch for this!


##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct

AMPATCH_FW_LOC1 = 0x62A2  # 0B E0  | B loc_624C            -> 0E E0
AMPATCH_FW_LOC2 = 0x62B6  # 01 D8  | Bhi loc_624C          -> 04 D8
AMPATCH_FW_LOC3 = 0x62BC  # B0 7B  | LDRB R0, [R6,#0xE]    -> 01 E0

print('\n>>> Running',os.path.basename(sys.argv[0]),'mod...')

fw =  bytearray(open(sys.argv[1],'rb').read())

if fw[AMPATCH_FW_LOC1:AMPATCH_FW_LOC1+1] == b'\x0B' and fw[AMPATCH_FW_LOC2:AMPATCH_FW_LOC2+1] == b'\x01' and fw[AMPATCH_FW_LOC3:AMPATCH_FW_LOC3+2] == b'\xB0\x7B':
    print('Enabling AM on all frequency ranges...')
    fw[AMPATCH_FW_LOC1:AMPATCH_FW_LOC1+1] = b'\x0E'
    fw[AMPATCH_FW_LOC2:AMPATCH_FW_LOC2+1] = b'\x04'
    fw[AMPATCH_FW_LOC3:AMPATCH_FW_LOC3+2] = b'\x01\xE0'
else:
    print('ERROR: Cant find function')

open(sys.argv[1],'wb').write(fw)
print('Done')
