def bmp(rawdata, w, h):
    rawdata = bytes(reversed(rawdata))
    bitdata = b''
    
    if w<16:
        bitdata = b''.join([ bytes([rawdata[i],0,0,0]) for i in range(0,len(rawdata)) ])
    elif w<24:
        for i in range(len(rawdata)//2):
            bitdata += rawdata[i*2:i*2+2]+b'\x00\x00'

    return (b"BM"                  + #signature 2bytes \x42\x4D
            b"\x00\x00\x00\x00"    + #filesize  (ignored by most editors) 
            b"\x00\x00\x00\x00"    + #reserved
            b"\x3E\x00\x00\x00"    + #bfOffBits
            b"\x28\x00\x00\x00"    + #headerszie always 0x28
            bytes([w%0x100,w//0x100,0,0])+ #biWidth
            bytes([h%0x100,h//0x100,0,0])+ #biHeight
            b"\x01\x00"            + #planes always1
            b"\x01\x00"            + #bitcount 1=monochrome
            b"\x00\x00\x00\x00"    + #compression
            b"\x00\x00\x00\x00"+
            b"\x00\x00\x00\x00"+
            b"\x00\x00\x00\x00"+
            b"\x00\x00\x00\x00"+
            b"\x00\x00\x00\x00"+
            b"\xff\xff\xff\x00"    + #colors[0]
            b"\x00\x00\x00\x00"    + #colors[1]
            bytes(bitdata)
            )



def mem16toBmp(raw_mem,symbol_width):
    bmp_format = b''
    for s in range(0,len(raw_mem)//(symbol_width*2)):
        symb_offset = s*symbol_width*2
        for i in range(0,symbol_width):
            bmp_format += bytes([raw_mem[symb_offset+i],raw_mem[symb_offset+i+symbol_width],])
    return bmp_format




#===============================================================================================




fw = open('k5_v2.01.26_publish_dec_cut.bin','rb').read()


#Misc symbols @0xD348
with open('01_08px_symbols.bmp','wb') as f:
    data = fw[0xD348:0xD348+442]
    f.write(bmp(data,8,len(data)))




#Big digits @0xD502
with open('02_16px_digits.bmp','wb') as f:
    data = fw[0xD502:0xD502+286]
    f.write(bmp(data,8,len(data)))

with open('03_16px_digits_stitched.bmp','wb') as f:
    data = mem16toBmp(fw[0xD502:0xD502+286],13)
    f.write(bmp(data,16,len(data)//2))




#Small digits @0xD620
with open('04_8px_digits.bmp','wb') as f:
    data = fw[0xD620:0xD620+84]
    f.write(bmp(data,8,len(data)))




#Full alphabet @0xD66D
with open('05_16px_alphabet.bmp','wb') as f:
    data = fw[0xD66D:0xD66D+ 16*95] # 95 characters, 16 bytes each
    f.write(bmp(data,8,len(data)))

with open('06_16px_alphabet_stitched.bmp','wb') as f:
    data = mem16toBmp(fw[0xD66D:0xD66D+ 16*95],8)
    f.write(bmp(data,16,len(data)//2))




#All of above in one
with open('07_complete.bmp','wb') as f:
    data = fw[0xD348:0xD66D+ 16*95] # 95 characters, 16 bytes each
    f.write(bmp(data,8,len(data)))
