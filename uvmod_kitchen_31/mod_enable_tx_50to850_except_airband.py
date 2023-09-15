# set values to block band
block_freq_lo = 118_000_000
block_freq_hi = 137_000_000



##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct
print('Running',os.path.basename(sys.argv[0]),'mod...')
fw =  bytearray(open(sys.argv[1],'rb').read())

addr = 0x182c

shellcode = b'\xF0\xB5\x01\x46\x49\x69\x09\x68\x05\x4A\x91\x42\x05\xD3\x05\x4A\x91\x42\x02\xD2\x00\x20\xC0\x43\x01\xE0\x00\x20\xFF\xE7\xF0\xBD'+bytearray(struct.pack('<II', block_freq_lo//10, block_freq_hi//10))
fw[addr:addr+len(shellcode)] = shellcode




open(sys.argv[1],'wb').write(fw)
