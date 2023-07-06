import serial
import struct
import os


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


def firmware_xor(fwcontent):
    XOR_ARRAY = bytes.fromhex('4722c0525d574894b16060db6fe34c7cd84ad68b30ec25e04cd9007fbfe35405e93a976bb06e0cfbb11ae2c9c15647e9baf142b6675f0f96f7c93c841b26e14e3b6f66e6a06ab0bfc6a5703aba189e271a535b71b1941e18f2d6810222fd5a2891dbba5d64c6fe86839c501c730311d6af30f42c77b27dbb3f29285722d6928b')
    XOR_LEN   = len(XOR_ARRAY)

    ba=bytearray(fwcontent)
    for i in range(0,len(ba)):
        ba[i] ^= XOR_ARRAY[i%XOR_LEN]
    return bytes(ba)


def payload_xor(payload):
    XOR_ARRAY = bytes.fromhex('166c14e62e910d402135d5401303e980')
    XOR_LEN   = len(XOR_ARRAY)

    ba=bytearray(payload)
    for i in range(0,len(ba)):
        ba[i] ^= XOR_ARRAY[i%XOR_LEN]
    return bytes(ba)

#================================================================================================================



class uvk5:
    def __enter__(self):
        return self
    def __exit__(self, type, value, traceback):
        pass

    def __init__(self,portName='COM1'):
        
        self.serial = serial.Serial()
        self.serial.baudrate = 38400
        self.serial.timeout=1
        self.serial.port=portName
        self.sessTimestamp = b'\x46\x9C\x6F\x64'

        self.CMD_GET_FW_VER   = b'\x14\x05' #0x0514 -> 0x0515
        self.CMD_READ_FW_MEM  = b'\x17\x05' #0x0517 -> 0x0518
        self.CMD_WRITE_FW_MEM = b'\x19\x05' #0x0519 -> 0x051a //Only in bootloader

        self.CMD_READ_CFG_MEM = b'\x1B\x05' #0x051B -> 0x051C
        self.CMD_WRITE_CFG_MEM= b'\x1D\x05' #0x051D -> 0x051E


        self.CMD_052D         = b'\x2D\x05'
        self.CMD_051F         = b'\x1F\x05'
        self.CMD_052F         = b'\x2F\x05'
        
        self.CMD_REBOOT       = b'\xDD\x05' #0x05DD -> no reply
        self.CMD_0530         = b'\x30\x05' #0x0530 -> no reply //Only in bootloader
        self.CMD_0527         = b'\x27\x05'
        
        self.debug = False if os.getenv('DEBUG') is None else True

    def __del__(self):
        self.serial.close()
        return not self.serial.is_open




    def connect(self):
        self.serial.open()
        return self.serial.is_open

    def uart_send_msg(self,msg_dec):
        if self.debug: print('>dec>',msg_dec.hex())
        msg_raw = msg_dec[:4] + payload_xor(msg_dec[4:-2]) + msg_dec[-2:]
        if self.debug: print('>raw>',msg_raw.hex())
        return self.serial.write(msg_raw)

    def uart_receive_msg(self,len):
        msg_raw = self.serial.read(len)
        if self.debug: print('<raw<',msg_raw.hex())
        msg_dec = msg_raw[:4] + payload_xor(msg_raw[4:-2]) + msg_raw[-2:]
        if self.debug: print('<dec<',msg_dec.hex())
        return msg_dec


    def build_uart_command(self, command_type, command_body=b''):
        cmd = command_type + struct.pack('<H',len(command_body))+ command_body
        cmd_len = struct.pack('<H',len(cmd))
        cmd_crc = struct.pack('<H',crc16_ccitt(cmd))
        cmd =  b'\xAB\xCD' + cmd_len + cmd + cmd_crc + b'\xDC\xBA'
        return cmd


    def get_fw_version(self):
        cmd=self.build_uart_command(self.CMD_GET_FW_VER, self.sessTimestamp)
        self.uart_send_msg(cmd)
        reply = self.uart_receive_msg(128)
        return reply[8:].split(b'\0', 1)[0].decode()

    def get_cfg_mem(self,address,length):
        cmd=self.build_uart_command(self.CMD_READ_CFG_MEM, struct.pack('<HH',address,length) + self.sessTimestamp)
        self.uart_send_msg(cmd)
        reply = self.uart_receive_msg(length+16)
        return reply[12:-4]
        
    def set_cfg_mem(self,address,payload):
        if len(payload)%8==0:
            cmd=self.CMD_WRITE_CFG_MEM + struct.pack('<HHH',len(payload)+8, address, len(payload)) + self.sessTimestamp + payload
            cmd_crc = struct.pack('<H',crc16_ccitt(cmd))
            cmd=b'\xAB\xCD' + struct.pack('<H',len(payload)+0xC) + cmd + cmd_crc + b'\xDC\xBA'
            self.uart_send_msg(cmd)
            reply = self.uart_receive_msg(14)
            return reply[12:-4]
        else:
            raise Exception('Payload have to be multiples of 8 bytes')
        
    def reboot(self):
        cmd = self.CMD_REBOOT + b'\x00\x00'
        cmd_crc = struct.pack('<H',crc16_ccitt(cmd))
        cmd= b'\xAB\xCD' + struct.pack('<H',4) + cmd + cmd_crc + b'\xDC\xBA'
        self.uart_send_msg(cmd)
        return True

    def get_fw_mem(self,address,length):
        cmd=self.CMD_READ_FW_MEM #+ b'\x00\x00' # struct.pack('<HH',address,length)
        cmd= b'\x00\x05' #+ b'\x00\x00' # struct.pack('<HH',address,length)
        cmd_crc =  b'' #struct.pack('<H',crc16_ccitt(cmd))
        cmd=b'\xAB\xCD' + struct.pack('<H',len(cmd)) + cmd + cmd_crc + b'\xDC\xBA'
        self.uart_send_msg(cmd)
        reply = self.uart_receive_msg(1024)
        return reply[12:-4]

    #def set_fw_mem(self,block,payload):
    #    bytes_to_write = length(payload)
    #    padd_bytes = b'\x00'*(1000 - bytes_to_write)
    #    payload=payload+padd_bytes
    #    print(payload.hex())
    #    cmd=self.build_uart_command(self.CMD_WRITE_FW_MEM,  struct.pack('<IIII',block,bytes_to_write,0xe6,0) + self.sessTimestamp + payload)
    #    self.uart_send_msg(cmd)
    #    reply = self.uart_receive_msg(128)
    #    return reply[12:-4]
        
    def unk_fn_0530(self,text):
        buff = bytes(text,'ascii') + b'\x00'*(16-len(text))
        cmd = self.CMD_0530 + struct.pack('<H',16) + buff
        cmd_crc = struct.pack('<H',crc16_ccitt(cmd))
        cmd= b'\xAB\xCD' + struct.pack('<H',20) + cmd + cmd_crc + b'\xDC\xBA'
        self.uart_send_msg(cmd)
        reply = self.uart_receive_msg(128)
        return reply[12:-4]
        
    def unk_fn_051F(self):
        #          0/1      +        2/3           
        cmd = self.CMD_051F + struct.pack('<H',18)+ \
                struct.pack('<I',433000000) +        \
                struct.pack('<H',0x00) +           \
                struct.pack('<H',0x7F) +           \
                struct.pack('<H',0xFF) +           \
                struct.pack('<H',0x00) +           \
                struct.pack('<H',0x7F) +           \
                struct.pack('<H',0xFF) +           \
                struct.pack('<H',1)                   
                
        cmd_crc = struct.pack('<H',crc16_ccitt(cmd))
        cmd= b'\xAB\xCD' + struct.pack('<H',22) + cmd + cmd_crc + b'\xDC\xBA'
        self.uart_send_msg(cmd)
        reply = self.uart_receive_msg(128)
        return reply[12:-4]

    def unk_fn_052F(self):
        #          0/1      +        2/3           
        cmd = self.CMD_052F + struct.pack('<H',4) + self.sessTimestamp
                
        cmd_crc = struct.pack('<H',crc16_ccitt(cmd))
        cmd= b'\xAB\xCD' + struct.pack('<H',8) + cmd + cmd_crc + b'\xDC\xBA'
        self.uart_send_msg(cmd)
        reply = self.uart_receive_msg(128)
        return reply[12:-4]


    def unk_fn_1325(self,uint1,uint2,uint3,uint4):
        cmd = self.CMD_052D + struct.pack('<HIIII',16,uint1,uint2,uint3,uint4)
        cmd_crc = struct.pack('<H',crc16_ccitt(cmd))
        cmd= b'\xAB\xCD' + struct.pack('<H',20) + cmd + cmd_crc + b'\xDC\xBA'
        self.uart_send_msg(cmd)
        reply = self.uart_receive_msg(128)
        return reply[12:-4]
        
    def get_rssi(self):
        cmd = self.CMD_0527 + struct.pack('<H',4) + self.sessTimestamp
        cmd_crc = struct.pack('<H',crc16_ccitt(cmd))
        cmd = b'\xAB\xCD' + struct.pack('<H',8) + cmd + cmd_crc + b'\xDC\xBA'
        self.uart_send_msg(cmd)
        reply = self.uart_receive_msg(16)
        rssi,noise,glitch = struct.unpack('<HBB',reply[8:-4])
        rssi = rssi / 2 - 160
        return {'rssi':rssi, 'noise':noise, 'glitch':glitch, 'raw':reply[8:-4].hex()}
