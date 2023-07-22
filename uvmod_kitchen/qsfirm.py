import sys,os


# Handle arguments 
if len(sys.argv)!=5 or sys.argv[1] not in ['unpack','pack'] : print(f'''
Usage: {os.path.basename(sys.argv[0])} unpack <encoded_firmware_in.bin> <decoded_firmware_out.bin> <versionfile_out.bin>
       {os.path.basename(sys.argv[0])} pack <decoded_firmware_in.bin> <versionfile_in.bin> <encoded_firmware_out.bin>
       ''') ; exit(1)

# CRC Routines
Crc16Tab = [0, 4129, 8258, 12387, 16516, 20645, 24774, 28903, 33032, 37161, 41290, 45419, 49548, 53677, 57806, 61935, 4657, 528, 12915, 8786, 21173, 17044, 29431, 25302,
            37689, 33560, 45947, 41818, 54205, 50076, 62463, 58334, 9314, 13379, 1056, 5121, 25830, 29895, 17572, 21637, 42346, 46411, 34088, 38153, 58862, 62927, 50604, 54669, 13907,
            9842, 5649, 1584, 30423, 26358, 22165, 18100, 46939, 42874, 38681, 34616, 63455, 59390, 55197, 51132, 18628, 22757, 26758, 30887, 2112, 6241, 10242, 14371, 51660, 55789,
            59790, 63919, 35144, 39273, 43274, 47403, 23285, 19156, 31415, 27286, 6769, 2640,14899, 10770, 56317, 52188, 64447, 60318, 39801, 35672, 47931, 43802, 27814, 31879,
            19684, 23749, 11298, 15363, 3168, 7233, 60846, 64911, 52716, 56781, 44330, 48395,36200, 40265, 32407, 28342, 24277, 20212, 15891, 11826, 7761, 3696, 65439, 61374,
            57309, 53244, 48923, 44858, 40793, 36728, 37256, 33193, 45514, 41451, 53516, 49453, 61774, 57711, 4224, 161, 12482, 8419, 20484, 16421, 28742, 24679, 33721, 37784, 41979,
            46042, 49981, 54044, 58239, 62302, 689, 4752, 8947, 13010, 16949, 21012, 25207, 29270, 46570, 42443, 38312, 34185, 62830, 58703, 54572, 50445, 13538, 9411, 5280, 1153, 29798,
            25671, 21540, 17413, 42971, 47098, 34713, 38840, 59231, 63358, 50973, 55100, 9939, 14066, 1681, 5808, 26199, 30326, 17941, 22068, 55628, 51565, 63758, 59695, 39368,
            35305, 47498, 43435, 22596, 18533, 30726, 26663, 6336, 2273, 14466, 10403, 52093, 56156, 60223, 64286, 35833, 39896, 43963, 48026, 19061, 23124, 27191, 31254, 2801,
            6864, 10931, 14994, 64814, 60687, 56684, 52557, 48554, 44427, 40424, 36297, 31782, 27655, 23652, 19525, 15522, 11395, 7392, 3265, 61215, 65342, 53085, 57212, 44955,
            49082, 36825, 40952, 28183, 32310, 20053, 24180, 11923, 16050, 3793, 7920]

def crc16_ccitt(data):
    i2 = 0
    for i3 in range(0, len(data)):
        out = Crc16Tab[((i2 >> 8) ^ data[i3]) & 255]
        i2 = out ^ (i2 << 8)
    return 65535 & i2

def crc16_ccitt_le(data):
    crc = crc16_ccitt(data)
    return bytes([crc & 0xFF,]) + bytes([crc>>8,])


# Encoding/decoding algo
def firmware_xor(fwcontent):
    XOR_ARRAY = bytes.fromhex('4722c0525d574894b16060db6fe34c7cd84ad68b30ec25e04cd9007fbfe35405e93a976bb06e0cfbb11ae2c9c15647e9baf142b6675f0f96f7c93c841b26e14e3b6f66e6a06ab0bfc6a5703aba189e271a535b71b1941e18f2d6810222fd5a2891dbba5d64c6fe86839c501c730311d6af30f42c77b27dbb3f29285722d6928b')
    XOR_LEN   = len(XOR_ARRAY)

    ba=bytearray(fwcontent)
    for i in range(0,len(ba)):
        ba[i] ^= XOR_ARRAY[i%XOR_LEN]
    return bytes(ba)



#-------- main ------------------
if sys.argv[1]=='unpack':
    encoded_firmware =  open(sys.argv[2],'rb').read()
    #check CRC, information only
    if crc16_ccitt_le(encoded_firmware[:-2]) == encoded_firmware[-2:]:
        print('CRC OK')
    else:
        print('CRC MISMATCH!')
    
    decoded_firmware = firmware_xor(encoded_firmware[:-2])
    
    #save decoded firmware to file
    open(sys.argv[3],'wb').write(decoded_firmware[:0x2000]+decoded_firmware[0x2000+16:])
    print(f'Saved decoded firmware to {sys.argv[3]}')

    #save 16 bytes with version string to file
    open(sys.argv[4],'wb').write(decoded_firmware[0x2000:0x2000+16])
    print(f'Saved version info to {sys.argv[4]}')




elif sys.argv[1]=='pack':
    decoded_firmware = open(sys.argv[2],'rb').read()

    # visual indicator for firmware size and big warning if too big
    current_size = len(decoded_firmware)
    max_size = 0xf000

    percentage = (current_size / max_size) * 100
    bar_length = int(percentage / 2)  # Assuming each character represents 2% progress
    size_bar = '[' + '=' * bar_length + ' ' * (50 - bar_length) + ']'

    print(f"\n\nFirmware takes up {current_size}/{max_size} bytes of available space:")
    print(f"Flash usage: {size_bar} {percentage:.2f}%\n\n")
    
    if current_size > max_size:
        print("WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING")
        print("WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING")
        print("WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING")
        print("WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING\n")
        print("WARNING: Firmware size exceeds the maximum allowed size of 0xf000 (61440) bytes!")
        print("Using an oversize firmware will not work correctly and may lead to freezes, crashes and defects.\n")
    
    
    version_info     = open(sys.argv[3],'rb').read()[0:16]
    
    firmware_with_version = decoded_firmware[0:0x2000] + version_info + decoded_firmware[0x2000:]
    firmware_with_version_encoded = firmware_xor(firmware_with_version)
    
    open(sys.argv[4],'wb').write(firmware_with_version_encoded+crc16_ccitt_le(firmware_with_version_encoded))
    print(f'Saved encoded firmware to {sys.argv[4]}')

