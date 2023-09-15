# If you want, configure these two parameters to change the frequencies of the two tones.
# The delay, sadly, is fixed to (tone 1 for 150ms), (tone 2 for 80ms) for now because I'm lazy.
tone1 = int(1540 * 10.32444) # change 1540 to any frequency in Hz
tone2 = int(1310 * 10.32444) # change 1310 to any frequency in Hz

##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct
print('Running',os.path.basename(sys.argv[0]),'mod...')

fw =  bytearray(open(sys.argv[1],'rb').read())

addr1 = 0xAED0
addr2 = 0xAE9A

if fw[addr1:addr1+4] == struct.pack('<I',0x142a) and fw[addr1+4:addr1+8] == struct.pack('<I',0x1c3b):
    print('Changing roger beep tones...')
    fw[addr1:addr1+4] = struct.pack('<I',tone1)
    fw[addr1+4:addr1+8] = struct.pack('<I',tone2)
    fw[addr2] = 0x96
else:
    print('ERROR: Cant find function')


open(sys.argv[1],'wb').write(fw)

