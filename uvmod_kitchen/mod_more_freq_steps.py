# change below steps to new ones, values are in Hz
# You can add reasonably more steps here

new_freq_steps = [2500, 5000, 6250, 10000, 12500, 25000, 8330, 500000, 10, 1250, 20000]




##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct

print('Running',os.path.basename(sys.argv[0]),'mod...')



fw =  bytearray(open(sys.argv[1],'rb').read())
new_freq_array_offset = bytearray(struct.pack('<I',len(fw)))


new_freq_len = len(new_freq_steps)
new_freq_array = bytearray(struct.pack('<'+'H'*new_freq_len, *[i//10 for i in new_freq_steps]))

#print(new_freq_array.hex())
#print(new_freq_array_offset.hex())


#append new array to FW
fw += new_freq_array


#replace references
fw[0x628C:0x628C+4] = new_freq_array_offset
fw[0x986C:0x986C+4] = new_freq_array_offset

#replace table sizes
fw[0x609C] = new_freq_len
fw[0x2356] = new_freq_len-1
fw[0x2350] = new_freq_len-1


open(sys.argv[1],'wb').write(fw)
