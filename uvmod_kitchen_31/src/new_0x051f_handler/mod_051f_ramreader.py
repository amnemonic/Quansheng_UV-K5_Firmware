##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct
print('Running',os.path.basename(sys.argv[0]),'mod...')
fw =  bytearray(open(sys.argv[1],'rb').read())






shellcode = b'\x0A\x4B\x10\xB5\x1A\x88\x0A\x4B\x01\x2A\x0C\xD1\x09\x4A\x51\x88\x10\x88\x09\x4A\x09\x04\x01\x43\x50\x88\x14\x88\x00\x04\x20\x43\x98\x47\x00\x20\x10\xBD\x08\x21\x04\x48\xF9\xE7\x88\x05\x00\x20\x45\xBE\x00\x00\x8E\x05\x00\x20\x8A\x05\x00\x20\x44\x0D\x00\x00\x55\x6E\x6B\x6E\x20\x72\x65\x71\x00'


fw[0x0D04:0x0DF8] = b'\x00'*len(fw[0x0D04:0x0DF8])    # set all bytes in function to zeroes, just for aesthetics reasons
fw[0x0D04:0x0D04+len(shellcode)] = shellcode          # put new function code





open(sys.argv[1],'wb').write(fw)

