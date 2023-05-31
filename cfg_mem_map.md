Application "QS Portable Radio CPS" reads following areas of memory:

| Address| Length    | Content (probably)  |
| :---:  |  ---:     | :------  |
|`0x0E70`| `0xA8`    | Common settings + DTMF settings |
|`0x0D60`| `0xCF`    | MR Channels Parameters (format unknown) |
|`0x0F50`| `0x0C80`  | MR Channels names, 16 bytes/ch |
|`0x0000`| `0x0D60`  | MR Channels frequency, 16 bytes/ch * 200 + VFO Channels⁺, 16 bytes/ch * 14 |
|`0x1C00`| `0x0100`  | DTMF Contacts, 16 bytes/contact * 16 |  
|`0x0E40`| `0x28`    | FM channels⁺, 2 bytes/ch * 20 |
|`0x0F18`| `0x8`     | ? |

<hr>

Additional addresses found by trial and error:

| Address| Length    | Content (probably)  |
| :---:  |  ---:     | :------  |
|`0x0E97`| `1`       | Power on display mode: `0`=Fullscreen, `1`=Welcome info, `2`=Voltage |
|`0x0EB0`| `0x10`      | `Quansheng` string (welcome screen)
|`0x0EC0`| `0x10`      | `UV-K5` string (welcome screen, 2 line)
|`0x0F40`| `1`       | F-LOCK: `0`=Off, `1`=FCC, `2`=CE, `3`=GB, `4`=430, `5`=438 |
|`0x0F41`| `1`       | 350TX: `01`=On, `00`=Off |
|`0x0F42`| `1`       | ? |
|`0x0F43`| `1`       | 200TX: `01`=On, `00`=Off |
|`0x0F44`| `1`       | 500TX: `01`=On, `00`=Off |
|`0x0F45`| `1`       | 350EN: `01`=On, `00`=Off |
|`0x0F46`| `1`       | SCREEN: `01`=On, `00`=Off |


⁺ Side note: all frequencies are stored as follows: 446.05625MHz is just 0x02A8A0B9 (44605625 in hex) with the bytes reversed (so the EEPROM contains B9 A0 A8 02.) For the FM channels, only 3 digits are used and the zeroes are cut, e.g. 91.1 FM becomes 911, 38F in hex, stored as 8F 03.
