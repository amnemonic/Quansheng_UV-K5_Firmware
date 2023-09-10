# change below sets to new ones, values are in Hz
new_freq_low_limit =   [18_000_000,  76_000_000, 136_000_000, 174_000_000, 350_000_000, 400_000_000,  470_000_000]
new_freq_high_limit =  [75_999_900, 135_999_900, 173_999_900, 349_999_900, 399_999_900, 469_999_900, 1300_000_000]



##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct

LOFREQ_FW_LOC = 0xE100  #v2.01.31
HIFREQ_FW_LOC = 0xE11C  #v2.01.31

print('\n>>> Running',os.path.basename(sys.argv[0]),'mod...')

#prechecks
if len(new_freq_low_limit)!=7: print('Do not change number of entries! Exiting'); exit(0)
if len(new_freq_high_limit)!=7: print('Do not change number of entries! Exiting'); exit(0)


#read fw to buffer
fw =  bytearray(open(sys.argv[1],'rb').read())

#Show old ranges
print('Replacing ranges:')
current_lo_limits = struct.unpack_from('<IIIIIII', fw, offset=LOFREQ_FW_LOC)
current_hi_limits = struct.unpack_from('<IIIIIII', fw, offset=HIFREQ_FW_LOC)
for i in range(7): 
    print('Range F{} {:>11} Hz -{:>11} Hz -->  {:>11} Hz -{:>11} Hz'.format(i+1,
        current_lo_limits[i]*10 ,
        current_hi_limits[i]*10 , 
        new_freq_low_limit[i]   , 
        new_freq_high_limit[i] 
    ))






## REPLACE LOFREQ
if fw[LOFREQ_FW_LOC:LOFREQ_FW_LOC+(4*7)] == bytearray(struct.pack('<IIIIIII', *[5000000, 10800000, 13600000, 17400000, 35000000, 40000000, 47000000])):
    print('LOFREQ table found, replacing...')
    fw[LOFREQ_FW_LOC:LOFREQ_FW_LOC+(4*7)] = bytearray(struct.pack('<IIIIIII', *[i//10 for i in new_freq_low_limit]))
else:
    print('Error, orginal LOFREQ table doesnt match default values. Wrong fw ver?')
    
    
## REPLACE HIFREQ
if fw[HIFREQ_FW_LOC:HIFREQ_FW_LOC+(4*7)] == bytearray(struct.pack('<IIIIIII', *[7600000, 13599990, 17399990, 34999990, 39999990, 46999990, 60000000])):
    print('HIFREQ table found, replacing...')
    fw[HIFREQ_FW_LOC:HIFREQ_FW_LOC+(4*7)] = bytearray(struct.pack('<IIIIIII', *[i//10 for i in new_freq_high_limit]))
else:
    print('Error, orginal HIFREQ table doesnt match default values. Wrong fw ver?')




#write fw back
open(sys.argv[1],'wb').write(fw)
