# TOC
At the beginning I was planning to put here only official firmwares found somewhere in update files and internet but now, with help from people involved in process of reverse enginnering of uvk5 you can find here some knowledge and findings regarding our very wallet friendly yet so capable radio. Here is table of contents of this repository.

## Build your own firmware - [/uvmod_kitchen](/uvmod_kitchen)
You can select what you want to include in your modded firmware. If you want unlock all frequencies but also have custom frequency steps? This is section for you. Thanks to this tool you can mix and match different mods to be included in final firmware. All mods are basing on firmware version k5_2.01.26.

## Documents - [/docs](/docs)
Some (incomplete) documents with info about CPU I/O pins, memory mappings, firmware format etc. 

## Font and graphics - [/font_and_graphics](/font_and_graphics)
Simple python script which extracts from firmware all bitmaps used in radio's user interface. It works as substitute of documentation.

## Datasheets and drawings - [/hardware](/hardware)
Here are all the efforts of searching internet for datasheets but also drawings of reverse engineered schematics and high resolution photos of PCB.

## OpenOCD configs - [/openocd](/openocd)
Tools necessary to unbrick your radio or dump flash memory.

## Utility scripts - [/python-utils](/python-utils)
Python library and sample scripts which leverage official communication protocol. You can dump EEPROM and reboot your radio or decode firmware. 

## Quansheng UV-K5 Firmware collection - [/firmware](/firmware)
Only stock firmwares, no mods, no alterations. If you want modified firmware ready to flash please check out [Andrej](https://github.com/Tunas1337/UV-K5-Modded-Firmwares)'s repo

| Firmware_Version                                 | Programming software                                | Firmware-Updater |
| --                                               | --                                                  | --               |
| [k5_2.01.17](firmware/k5_v2.01.17_publish.bin)   |                                                     |                  |
| [k5_2.01.19](firmware/k5_v2.01.19_publish.bin)   |                                                     | 1.1.11           |
| [k5_2.01.23](firmware/k5_v2.01.23_publish.bin)   | V1.0.38 2023-02-11 07:49:36                         | 1.1.11           |
| [k5_2.01.25](firmware/k5_v2.01.25_publish.bin)   | Not released, dumped from device                    | n/a              |
| [k5_2.01.26](firmware/k5_v2.01.26_publish.bin)   | V1.0.38                                             | 1.1.12           |
| [k5_2.01.27](firmware/k5_v2.01.27_flashable.bin) | Not released, dumped from device by @CloverGit      | n/a              |
| [k5_3.00.10](firmware/k5_v3.00.10_flashable.bin) | Not released, dumped from device (**UV-K6**)        | n/a              |
| [k5_4.00.01](firmware/k5_v4.00.01_flashable.bin) | Not released, dumped from device (**UV-5R PLUS**)   | n/a              |

All files from table are already encoded and can be directly flashed using firmware updater V1.1.12. 

# Links
* [ludwich66 - Quansheng UV-K5 Wiki](https://github.com/ludwich66/Quansheng_UV-K5_Wiki/wiki)
* [Tunas1337 - UV-K5-Modded-Firmwares](https://github.com/Tunas1337/UV-K5-Modded-Firmwares)
* [sq5bpf - uvk5-reverse-engineering](https://github.com/sq5bpf/uvk5-reverse-engineering) | [CHIRP Driver](https://github.com/sq5bpf/uvk5-reverse-engineering/blob/main/uvk5.py) | [Official CHIRP Driver](https://github.com/kk7ds/chirp/blob/master/chirp/drivers/uvk5.py)
* [fagci - qs-uvk5-firmware-modder](https://github.com/fagci/qs-uvk5-firmware-modder)
* [piotr022 - UV_K5_playground](https://github.com/piotr022/UV_K5_playground)
* [manujedi - UV_K5-Tools](https://github.com/manujedi/UV_K5-Tools)
* [dkxce - Quansheng-UV-K5](https://github.com/dkxce/Quansheng-UV-K5)
* [Hackaday article 🛠](https://hackaday.com/2023/06/23/easy-modifications-for-inexpensive-radios/)
* [Telegram Channel - Global](https://t.me/quansheng_uvk5_en)
* [Telegram Channel - 🇷🇺 RU](https://t.me/uv_k5)
* [Telegram Channel - 🇪🇸 ES -> First one](https://t.me/Quansenguvk5) 
* [Telegram Channel - 🇪🇸 ES -> Second channel](https://t.me/QuanShengES)
* [Telegram Channel - 🇮🇹 IT](https://t.me/+W31XPFpurWk0NzM0)
* [Telegram Channel - 🇵🇱 PL](https://t.me/uvk5_pl)
* [Telegram Channel - 🇩🇪 DE](https://t.me/quanshenguv5kde)
* [Telegram Channel - 🇺🇦 UA](https://t.me/radioamators/38782)
* Official UV-K5 support page:              [Chinese](http://qsfj.com/support/downloads/3002) | [English](http://en.qsfj.com/support/downloads/3002)
* Official UV-K5 product page:              [Chinese](http://qsfj.com/products/3002)          | [English](http://en.qsfj.com/products/3002)
* Official UV-K5(8) aka UV-K6 support page: [Chinese](http://qsfj.com/support/downloads/3268) | [English](http://en.qsfj.com/support/downloads/3268)
* Official UV-K5(8) aka UV-K6 product page: [Chinese](http://qsfj.com/products/3268)          | [English](http://en.qsfj.com/products/3268)
* [FCC Reports](https://fcc.id/XBPUV-K5) / [fcc.gov](https://apps.fcc.gov/oetcf/eas/reports/ViewExhibitReport.cfm?mode=Exhibits&RequestTimeout=500&calledFromFrame=Y&application_id=8sqkxgC%2F1cYNHF0lGkSAwA%3D%3D&fcc_id=XBPUV-K5)
* [DP32G030 Product page](https://dnsj88.com/dp32g030lq32)
* [DP32G030 Datasheet](https://dnsj88.com/filedownload/493463)
* [Google Drive folder with useful info](https://drive.google.com/drive/folders/1NmcPb5yl5jnz7uWBO-c4B89XYL5AZeHw)
* Facebook - [Quansheng Electronics Co., Ltd.](https://www.facebook.com/QuanshengRadios/)
* Facebook - [Quansheng UV-K5 User's Group](https://www.facebook.com/groups/229333669483573/)
* Facebook - [QuanSheng UV-K5 UV-K5(8) UV-K6 - Polska](https://www.facebook.com/groups/205485455659292/)
* Facebook - [Quansheng UV-K5 UK Users](https://www.facebook.com/groups/2291286734508728/)
* Facebook - [Quansheng UV-K5 Philippines User Group](https://www.facebook.com/groups/678587170703812/)


### Thanks for all contributors

<a href="https://github.com/amnemonic/Quansheng_UV-K5_Firmware/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=amnemonic/Quansheng_UV-K5_Firmware" />
</a>
