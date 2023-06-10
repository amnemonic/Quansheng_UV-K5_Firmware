# change below frequencies to new ones, values are in Hz

#stock values
#new_noaa_table =   [162_550_000, 162_400_000, 162_475_000, 162_425_000, 162_450_000, 162_500_000, 162_525_000, 161_525_000, 161_775_000, 163_275_000 ]


#first 10 PMR446 channels
new_noaa_table =   [446_006_250, 446_018_750, 446_031_250, 446_043_750, 446_056_250, 446_068_750, 446_081_250, 446_093_750, 446_106_250, 446_118_750,  ]

##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct

print('Running',os.path.basename(sys.argv[0]),'mod...')

if len(new_noaa_table)!=10: print('Do not change number of entries! Exiting'); exit(0)



fw =  bytearray(open(sys.argv[1],'rb').read())
current_noaa = struct.unpack_from('<10I', fw, offset=0xE0D8) ; print('Old noa freqs:', [f'{i*10} Hz' for i in current_noaa])



## REPLACE NOAA FREQS
fw[0xE0D8:0xE0D8+(4*10)] = bytearray(struct.pack('<10I', *[i//10 for i in new_noaa_table]))

current_noaa = struct.unpack_from('<10I', fw, offset=0xE0D8) ; print('New noa freqs:', [f'{i*10} Hz' for i in current_noaa])


open(sys.argv[1],'wb').write(fw)
