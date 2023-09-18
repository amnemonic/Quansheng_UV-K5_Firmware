import os,sys
from PIL import Image

bytes_arr = open(sys.argv[1],'rb').read()

image = Image.new('RGB', (128, 64))

byte_cnt=0
for row in range(8):
    for colmn in range(128):
        for bit in range(8):
            x=colmn
            y=8 * row + bit
            if (bytes_arr[byte_cnt] >> bit) & 0x1 == 1:
                image.putpixel((x, y), (0, 0, 0))
            else:
                image.putpixel((x, y), (255, 255, 255))
        byte_cnt+=1

image.save(sys.argv[2])