# change below sets to new ones, values are in Hz
new_freq_steps = [2500, 5000, 6250, 10000, 12500, 25000, 8330]



##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct
if len(new_freq_steps)!=7: print('Do not change number of entries'); exit(0)

print('Running',os.path.basename(sys.argv[0]),'mod...')

addr = 0xE170

fw =  bytearray(open(sys.argv[1],'rb').read())
current_steps = struct.unpack_from('<HHHHHHH', fw, offset=addr)
print('Old freq steps:', [f'{i*10} Hz' for i in current_steps])


if fw[addr   :addr+ 2] == bytearray(struct.pack('<H', 250)): fw[addr   :addr+ 2] = struct.pack('<H',new_freq_steps[0]//10); print('.',end='')
if fw[addr+ 2:addr+ 4] == bytearray(struct.pack('<H', 500)): fw[addr+ 2:addr+ 4] = struct.pack('<H',new_freq_steps[1]//10); print('.',end='')
if fw[addr+ 4:addr+ 6] == bytearray(struct.pack('<H', 625)): fw[addr+ 4:addr+ 6] = struct.pack('<H',new_freq_steps[2]//10); print('.',end='')
if fw[addr+ 6:addr+ 8] == bytearray(struct.pack('<H',1000)): fw[addr+ 6:addr+ 8] = struct.pack('<H',new_freq_steps[3]//10); print('.',end='')
if fw[addr+ 8:addr+10] == bytearray(struct.pack('<H',1250)): fw[addr+ 8:addr+10] = struct.pack('<H',new_freq_steps[4]//10); print('.',end='')
if fw[addr+10:addr+12] == bytearray(struct.pack('<H',2500)): fw[addr+10:addr+12] = struct.pack('<H',new_freq_steps[5]//10); print('.',end='')
if fw[addr+12:addr+14] == bytearray(struct.pack('<H', 833)): fw[addr+12:addr+14] = struct.pack('<H',new_freq_steps[6]//10); print('.',end='')
print()


current_steps = struct.unpack_from('<HHHHHHH', fw, offset=addr)
print('New freq steps:', [f'{i*10} Hz' for i in current_steps])



open(sys.argv[1],'wb').write(fw)
