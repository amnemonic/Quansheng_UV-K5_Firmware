# change below sets to new ones, values are in Hz
new_freq_low_limit =   [50000000, 108000000, 136000000, 174000000, 350000000, 400000000, 470000000]
new_freq_high_limit =  [76000000, 135999900, 173999900, 349999900, 399999900, 469999900, 600000000]



##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct

print('Running',os.path.basename(sys.argv[0]),'mod...')

if len(new_freq_low_limit)!=7: print('Do not change number of entries! Exiting'); exit(0)
if len(new_freq_high_limit)!=7: print('Do not change number of entries! Exiting'); exit(0)


fw =  bytearray(open(sys.argv[1],'rb').read())
current_steps = struct.unpack_from('<IIIIIII', fw, offset=0xE074) ; print('Old freq ranges:', [f'{i*10} Hz' for i in current_steps])
current_steps = struct.unpack_from('<IIIIIII', fw, offset=0xE090) ; print('Old freq ranges:', [f'{i*10} Hz' for i in current_steps])


## REPLACE LOW FREQS
if fw[0xE074:0xE074+(4*7)] == bytearray(struct.pack('<IIIIIII', *[5000000, 10800000, 13600000, 17400000, 35000000, 40000000, 47000000])):
    print('OK, lofreq table found, replacing')
    fw[0xE074:0xE074+(4*7)] = bytearray(struct.pack('<IIIIIII', *[i//10 for i in new_freq_low_limit]))
else:
    print('Error, orginal lofreq table doesnt match default values. Wrong fw ver?')
    
    

if fw[0xE090:0xE090+(4*7)] == bytearray(struct.pack('<IIIIIII', *[7600000, 13599990, 17399990, 34999990, 39999990, 46999990, 60000000])):
    print('OK, hifrew table found, replacing')
    fw[0xE090:0xE090+(4*7)] = bytearray(struct.pack('<IIIIIII', *[i//10 for i in new_freq_high_limit]))
else:
    print('Error, orginal lofreq table doesnt match default values. Wrong fw ver?')

current_steps = struct.unpack_from('<IIIIIII', fw, offset=0xE074) ; print('New freq ranges:', [f'{i*10} Hz' for i in current_steps])
current_steps = struct.unpack_from('<IIIIIII', fw, offset=0xE090) ; print('New freq ranges:', [f'{i*10} Hz' for i in current_steps])



open(sys.argv[1],'wb').write(fw)
