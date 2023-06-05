# change below sets to new ones, values are in Hz
new_freq_steps = [2500, 5000, 6250, 10000, 12500, 25000, 8330]



##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct
if len(new_freq_steps)!=7: print('Do not change number of entries'); exit(0)

print('Running',os.path.basename(sys.argv[0]),'mod...')


fw =  bytearray(open(sys.argv[1],'rb').read())
current_steps = struct.unpack_from('<HHHHHHH', fw, offset=0xE0C8)
print('Old freq steps:', [f'{i*10} Hz' for i in current_steps])


if fw[0xE0C8:0xE0C8+2] == bytearray(struct.pack('<H', 250)): fw[0xE0C8:0xE0C8+2] = struct.pack('<H',new_freq_steps[0]//10); print('.',end='')
if fw[0xE0CA:0xE0CA+2] == bytearray(struct.pack('<H', 500)): fw[0xE0CA:0xE0CA+2] = struct.pack('<H',new_freq_steps[1]//10); print('.',end='')
if fw[0xE0CC:0xE0CC+2] == bytearray(struct.pack('<H', 625)): fw[0xE0CC:0xE0CC+2] = struct.pack('<H',new_freq_steps[2]//10); print('.',end='')
if fw[0xE0CE:0xE0CE+2] == bytearray(struct.pack('<H',1000)): fw[0xE0CE:0xE0CE+2] = struct.pack('<H',new_freq_steps[3]//10); print('.',end='')
if fw[0xE0D0:0xE0D0+2] == bytearray(struct.pack('<H',1250)): fw[0xE0D0:0xE0D0+2] = struct.pack('<H',new_freq_steps[4]//10); print('.',end='')
if fw[0xE0D2:0xE0D2+2] == bytearray(struct.pack('<H',2500)): fw[0xE0D2:0xE0D2+2] = struct.pack('<H',new_freq_steps[5]//10); print('.',end='')
if fw[0xE0D4:0xE0D4+2] == bytearray(struct.pack('<H', 833)): fw[0xE0D4:0xE0D4+2] = struct.pack('<H',new_freq_steps[6]//10); print('.',end='')
print()


current_steps = struct.unpack_from('<HHHHHHH', fw, offset=0xE0C8)
print('New freq steps:', [f'{i*10} Hz' for i in current_steps])



open(sys.argv[1],'wb').write(fw)