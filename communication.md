# General protocol description

All informations are gathered during monitoring of serial communication between device and orginal software.

* Data transmitted as little-endian (lower byte transmitted first)
* Communication on uart with baudrate 38400bps
* Offset `0x0`: Every message starts with `0xAB` `0xCD` bytes (`0xCDAB`)
* Offset `0x2`: Next comes two bytes with payload size.
* Offset `0x4`: Payload encoded using xor function described below.
* Next comes checksum of payload, size=2 bytes
* Finally every message ends with `0xDC` `0xBA` (`0xBADC`)


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


# Examples
## Get firmware version
command `0x0515` and reply `0x0514`
```python
import serial
import struct

with serial.Serial('COM14', 38400, timeout=1) as ser:
    tosend = 'abcd'+'0800'+'026910e6b1dd5824'+'2bdf'+'dcba'  #header + payload len + payload(encoded) + checksum + eot
    print('>>',tosend)
    ser.write(bytes.fromhex(tosend))
    full_response = ser.read(128)
    payload_decoded  = payload_xor(full_response[4:-4]) #skip header and checksum
    print('<<',full_response.hex())
    print(payload_decoded.hex())
    s = struct.unpack_from('<HH20s',payload_decoded)
    print('CMD: 0x{:04X}'.format(s[0]))
    print('LEN: 0x{:04X}'.format(s[1]))
    print('VER: {}'.format(s[2].split(b'\0', 1)[0].decode())) #null terminated string
```
this should return something like this:
```
>> abcd0800026910e6b1dd58242bdfdcba
<< abcd2800036930e645a452720f05e46e2130e9802a8e14e62e910d4018bce32a8b09e893c2862fd4b942e779decadcba
150524006b355f322e30312e323300003ce20000000000003989366a980a0113d4ea3b3297d3ea39
CMD: 0x0515
LEN: 0x0024
VER: k5_2.01.23
```
Lets analyze payload sent in request: `tosend = 'abcd'+'0800'+'026910e6b1dd5824'+'2bdf'+'dcba'`

`payload_xor(026910e6b1dd5824) = 140504009f4c5564`
* `1405` - request type
* `0400` - 4 bytes long
* `9f4c5564` - unknown yet
