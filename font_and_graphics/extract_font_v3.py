'''
Author: @tywtyw2002

Description: Extract graphcs from firmware version k5_V3.00.10

https://gist.github.com/tywtyw2002/fc90f8f8305120c42973d30868ed227e#file-extract-py
https://github.com/amnemonic/Quansheng_UV-K5_Firmware/issues/67

'''



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


# k5_v2.01.26_publish_dec_cut.bin
FW_NAME = "fw.dec.bin"
fw = open(FW_NAME,'rb').read()

FW_MARK = 0x0000CED0# 0xD348

#Misc symbols @0xD348
with open('01_08px_symbols.bmp','wb') as f:
    data = fw[FW_MARK:FW_MARK+434]
    f.write(bmp(data,8,len(data)))


#Big digits @0xD502
BG_MARK = FW_MARK + 434
with open('02_16px_digits.bmp','wb') as f:
    data = fw[BG_MARK:BG_MARK+286]
    f.write(bmp(data,8,len(data)))

with open('03_16px_digits_stitched.bmp','wb') as f:
    data = mem16toBmp(fw[BG_MARK:BG_MARK+286],13)
    f.write(bmp(data,16,len(data)//2))




#Small digits @0xD620
SD_MARK = FW_MARK + 720
with open('04_8px_digits.bmp','wb') as f:
    data = fw[SD_MARK:SD_MARK+77]
    f.write(bmp(data,8,len(data)))


#Full alphabet @0xD66D 
# AL_MARK = 0xd138
AL_MARK = FW_MARK + 720 + 77
with open('05_16px_alphabet.bmp','wb') as f:
    data = fw[AL_MARK:AL_MARK+ 14*94] # 94 characters, 14 bytes each
    f.write(bmp(data,8,len(data)))

with open('06_16px_alphabet_stitched.bmp','wb') as f:
    data = mem16toBmp(fw[AL_MARK:AL_MARK+ 14*94],7)
    f.write(bmp(data,16,len(data)//2))

#Chinese alphabet
CJK_MARK = FW_MARK + 720 + 77 + 14*94
with open('07_16px_cjk_alphabet.bmp','wb') as f:
    data = fw[CJK_MARK:CJK_MARK+ 26 * 143] # 143 characters, 26 bytes each
    f.write(bmp(data,8,len(data)))

with open('07_16px_cjk_alphabet_stitched.bmp','wb') as f:
    data = mem16toBmp(fw[CJK_MARK:CJK_MARK+ 26 * 143], 13)
    f.write(bmp(data,16,len(data)//2))

#All of above in one
#with open('07_complete.bmp','wb') as f:
#    data = fw[FW_MARK:AL_MARK+ 16*95] # 95 characters, 16 bytes each
#    f.write(bmp(data,8,len(data)))

#with open('07_complete_stitched.bmp','wb') as f:
#    data = mem16toBmp(fw[FW_MARK:AL_MARK+ 16*95],8)
#    f.write(bmp(data,16,len(data)//2))
