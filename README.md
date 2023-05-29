# Quansheng UV-K5 Firmware collection

Date       | Firmware-Updater | Firmware_Version                      | Programming software
--         | --               | --                                    | --
           |                  | [k5_2.01.17](k5_v2.01.17.bin)         |  
2023/<05   | 1.1.11           | [k5_2.01.19](k5_v2.01.19_publish.bin) |  
2023/05    | 1.1.11           | [k5_2.01.23](k5_v2.01.23_publish.bin) | V1.0.38 2023-02-11 07:49:36
2023/05/09 | 1.1.12           | [k5_2.01.26](k5_v2.01.26_publish.bin) | V1.0.38


# Firmware format

Orginal firmware is XOR-ed with 128 bytes long key:

```
4722c0525d574894b16060db6fe34c7c
d84ad68b30ec25e04cd9007fbfe35405
e93a976bb06e0cfbb11ae2c9c15647e9
baf142b6675f0f96f7c93c841b26e14e
3b6f66e6a06ab0bfc6a5703aba189e27
1a535b71b1941e18f2d6810222fd5a28
91dbba5d64c6fe86839c501c730311d6
af30f42c77b27dbb3f29285722d6928b
```

In decoded file at offset 8192 (0x2000) firmware version string can be found. 

To prepare firmware file for sending to device you have to do 3 steps:
* decode file using above xor key
* cut 16 bytes at address 0x2000
* cut two last bytes (checksum)





# Links

* [Official downloads page](http://qsfj.com/support/downloads/3002)
* [Official product page](http://qsfj.com/products/3002)
* [FCC Reports](https://fcc.id/XBPUV-K5) / [fcc.gov](https://apps.fcc.gov/oetcf/eas/reports/ViewExhibitReport.cfm?mode=Exhibits&RequestTimeout=500&calledFromFrame=Y&application_id=8sqkxgC%2F1cYNHF0lGkSAwA%3D%3D&fcc_id=XBPUV-K5)
