Application "QS Portable Radio CPS" reads following areas of memory:

| Address| Length    | Content (propably)  |
| :---:  |  ---:     | :------  |
|`0x0E70`| `0xA8`    | Common settings + DTMF settigns |
|`0x0D60`| `0xCF`    | ? |
|`0x0F50`| `0x0C80`  | MR Channels names, 16 bytes/ch |
|`0x0000`| `0x0D60`  | MR Channels config, 16 bytes/ch * 200 + VFO Channels, 16 bytes/ch * 14 |
|`0x1C00`| `0x0100`  | DTMF Contacts, 16 bytes/contact * 16 |  
|`0x0E40`| `0x28`    | ? |
|`0x0F18`| `0x8`     | ? |

<hr>

Additionall addresses found by trial and error:

| Address| Length    | Content (propably)  |
| :---:  |  ---:     | :------  |
|`0x0F40`| `1`       | F-LOCK: `0`=Off, `1`=FCC, `2`=CE, `3`=GB, `4`=430, `5`=438 |
|`0x0F41`| `1`       | 350TX: `01`=On, `00`=Off |
|`0x0F42`| `1`       | ? |
|`0x0F43`| `1`       | 200TX: `01`=On, `00`=Off |
|`0x0F44`| `1`       | 500TX: `01`=On, `00`=Off |
|`0x0F45`| `1`       | 350EN: `01`=On, `00`=Off |
|`0x0F46`| `1`       | SCREEN: `01`=On, `00`=Off |
