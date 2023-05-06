# General protocol description

All informations are gathered during monitoring of serial communication between device and orginal software.

* Communication on uart with baudrate 38400bps
* Offset `0x0`: Every message starts with `0xAB` `0xCD` bytes
* Offset `0x2`: Next comes two bytes with payload size, low byte first.
* Offset `0x4`: Payload of size defined at `0x2` offset. Payload is encoded using xor function described below
* Next comes checksum of payload, size=2 bytes
* Every message ends with `0xDC` `0xBA`

# Payload decoding

Payload content is XOR-ed with 16 bytes long key:
```
166c14e62e910d402135d5401303e980
```
