# General protocol description

All informations are gathered during monitoring of serial communication between device and orginal software.

* All values transmitted as little-endian (lower byte transmitted first) until otherwise noted
* Communication on uart with baudrate 38400bps
* Every message starts with `0xAB` `0xCD` bytes (`0xCDAB`)
* Next comes two bytes with payload size - 2
* Then payload encoded using xor function described below
* Finally every message ends with `0xDC` `0xBA` (`0xBADC`)

This can be shown also like this:<br>
`message` = `0xAB` `0xCD` `len(payload)-2` `payload_xor(payload)` `0xDC` `0xBA`


before encoding payload contains:
* Command ID - 2 bytes little endian (for example 0x0514, 0x051B etc)
* Command body length + 4 (2 bytes)
* Command body (variable size, can be zero length too)
* Command Trailer (4 bytes, ignored by device, applications sends unix timestamp, in all my samples i use `0x9f` `0x4c` `0x55` `0x64` and it works)
* CRC16 of above data (2 bytes)

This can be show like this:<br>
`payload` = `cmd_id` `len(cmd_body)+4` `cmd_body` `cmd_trailer` `crc16(cmd_id;len(cmd_body)+4;cmd_body;cmd_trailer)`


# Payload decoding/encoding
Payload content is XOR-ed with 16 bytes long key:
```
166c14e62e910d402135d5401303e980
```

In samples presented on this page I will use below function to decode/encode payloads:
```python
def payload_xor(payload):
    XOR_ARRAY = bytes.fromhex('166c14e62e910d402135d5401303e980')
    XOR_LEN   = len(XOR_ARRAY)

    ba=bytearray(payload)
    for i in range(0,len(ba)):
        ba[i] ^= XOR_ARRAY[i%XOR_LEN]
    return bytes(ba)
```

and this to calculate checksums:
```python
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
```


# Command types
## Summary
| Cmd ID    | Reply ID | Description                                    | Remarks           |
|-----------|----------|------------------------------------------------|------------------ |
| `0x0514`  | `0x0515` | [Get Firmware Version](#get-firmware-version)  | Only in Main ROM  |
| `0x0516`  | `0x0517` | Write to NVR?                                  | Only in Flashing mode ℹ |
| none      | `0x0518` | Bootloader loop message                        | Only in Flashing mode until `0x0530` sent ℹ|
| `0x0519`  | `0x051A` | Write to Flash                                 | Only in Flashing mode ℹ |
| `0x051B`  | `0x051C` | EEProm Read                                    | Only in Main ROM  |
| `0x051D`  | `0x051E` | EEProm Write                                                    | Only in Main ROM  |
| `0x051F`  | `0x0520` | Sends value to Reg 0x3B of BK4819 (Crystal Frequency Low-16bit) | Only in Main ROM, works only in lock mode - see `0x052F` |
| `0x0521`  | `0x0522` | Similar as above but different                 | Only in Main ROM  |
| `0x0527`  | `0x0528` | Returns values of registers of BK4819: 0x67 (RSSI), 0x65 (Ex-noiseindicator) and 0x63 (Glitch indicator) | Only in Main ROM  |
| `0x0529`  | `0x052A` | Read some values from ADC                      | Only in Main ROM  |
| `0x052D`  | `0x052E` | Set Password                                   | Only in Main ROM  |
| `0x052F`  | `0x0515` | Lock mode + Reply FW Ver                       | Only in Main ROM  |
| `0x0530`  |          | Break BootLoader wait loop                     | Only in Flashing mode ℹ |
| `0x05DD`  | none     | Jump to 0x20000000 (Reset)                     | Only in Main ROM  |






## Get firmware version
command id = `0x0515`, command body length = `0`, reply id = `0x0514`
```python
import serial
import struct

with serial.Serial('COM14', 38400, timeout=1) as ser:
    payload = b'\x14\x05' + b'\x04\x00' + b'\x9f\x4c\x55\x64' #cmd_id + cmd_len (0+4) + unix timestamp LE
    crc = crc16_ccitt(payload)
    payload = payload + bytes([crc & 0xFF,]) + bytes([crc>>8,])  #swap bytes of crc to get little endian
    message = b'\xAB\xCD' + b'\x08\x00' + payload_xor(payload) + b'\xDC\xBA'
    print('>>',message.hex())
    ser.write(message)


    full_response = ser.read(128)
    print('<<',full_response.hex())
    payload_decoded  = payload_xor(full_response[4:-4]) #skip header and checksum
    s = struct.unpack_from('<HH20s',payload_decoded)
    print('CMD: 0x{:04X}'.format(s[0]))
    print('LEN: 0x{:04X}'.format(s[1]))
    print('VER: {}'.format(s[2].split(b'\0', 1)[0].decode())) #null terminated string
```
this should return something like this:
```
>> abcd0800026910e6b1dd58242bdfdcba
<< abcd2800036930e645a452720f05e46e2130e9802a8e14e62e910d4066c929359d488b9884eba7b453e58337decadcba
CMD: 0x0515
LEN: 0x0024
VER: k5_2.01.23
```



## Read configuration memory (eeprom)
command id = `0x051B`, command body length = `4`, reply id = `0x051C`

Device have 8kB of memory for configuration. It can be read using command `0x051B`. Format of payload (before encoding) is following:<br>
| Command ID    | len(cmd_body)+4 |  Address (0 - 0x1FF)  |   Length      | dummy timestamp            |    CRC16      |
|  :---:        |      :---:      |    :---:              |   :---:       | :----:                     |   :----:      |
| `0x1B` `0x05` | `0x08` `0x00`   | `0x00` `0x00`         | `0x10` `0x00` | `0x9f` `0x4c` `0x55` `0x64`| `0xFF` `0xFF` |


Python code for dumping whole configuration memory can be found here: [dump_cfg.py](dump_cfg.py)

Brief map of memory contents: [cfg_mem_map.md](cfg_mem_map.md)

## Write configuration memory (eeprom)
command id = `0x051D`, command body length = variable, reply id = `0x051E`

| Command ID    | len(cmd_body)+4 |  Address (0 - 0x1FF)  |   Length      | dummy timestamp            | payload           |    CRC16      |
|  :---:        |      :---:      |    :---:              |   :---:       | :----:                     | :----:            |   :----:      |
| `0x1D` `0x05` | `0x08` `0x00`   | `0x00` `0x00`         | `0x10` `0x00` | `0x9f` `0x4c` `0x55` `0x64`| `0x00` ... `0x00` | `0xFF` `0xFF` |

Note: Payload length have to be mulitple of 8 bytes. Address don't have to be aligned.

## Change password
command id = `0x052D`, command body length = `0x10`, reply id = `0x052E`, Reply length = `0x08`

| Command ID  | len(cmd_body)+4 |  uint0                |  uint1                |  uint2                |  uint3                |    CRC16      |
|  :---:      |      :---:      |    :---:              |    :---:              |    :---:              |    :---:              |   :----:      |
| `0x2D 0x05` | `0x10 0x00`     | `0x00 0x00 0x00 0x00` | `0x00 0x00 0x00 0x00` | `0x00 0x00 0x00 0x00` | `0x00 0x00 0x00 0x00` | `0xFF 0xFF` |

TODO: Figure how old and new password is stored in these 4 uints / 16 bytes

