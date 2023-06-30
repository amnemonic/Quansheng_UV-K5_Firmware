from PIL import Image
import PIL.ImageOps
import sys

if len(sys.argv)!=3: print('Usage: Alphabet_encode.py <input_bitmap.bmp> <output_python_patch.py>') ; exit(1)


def pil_8b1b(in_bytes):
    if len(in_bytes)!=8:
        return None
    b = (0b00000001 * bool(in_bytes[7])) + \
        (0b00000010 * bool(in_bytes[6])) + \
        (0b00000100 * bool(in_bytes[5])) + \
        (0b00001000 * bool(in_bytes[4])) + \
        (0b00010000 * bool(in_bytes[3])) + \
        (0b00100000 * bool(in_bytes[2])) + \
        (0b01000000 * bool(in_bytes[1])) + \
        (0b10000000 * bool(in_bytes[0]))
    return bytes([b,])

im = Image.open(sys.argv[1])
if im.size!=(760,16):
    print('Image size different than 760x16px. Exiting')
    exit(1)

# do some transformations on image
im = im.convert('1')
im = im.rotate(-90, expand=True)
im = PIL.ImageOps.invert(im)
im = list(im.getdata())

# change PIL format to raw bytes format
raw = b''
for i in range(len(im)//8):
    offset=i*8
    raw += pil_8b1b(im[offset:offset+8])

# deinterlace bytes
raw_deint=b''
for i in range(0,95): # 95 characters of 8px width
    for j in range(0,8):
        raw_deint += bytes( [ raw[(i*16)+j*2+1],] )
    for j in range(0,8):
        raw_deint += bytes( [ raw[(i*16)+j*2],] )


big_digits_patch = ''.join([f'\\x{i:02X}' for i in raw_deint])
print("alphabet=b'"+big_digits_patch+"'")

open('test.bin','wb').write(raw_deint)

with open(sys.argv[2],'w') as f, open('Alphabet_encode.template','r') as template:
    f.write(template.read().replace('{_ARRAY_}',big_digits_patch))
