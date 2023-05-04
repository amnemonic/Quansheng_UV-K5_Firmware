# Quansheng UV-K5 Firmware collection

* [Official downloads page](http://qsfj.com/support/downloads/3002)
* [Official product page](http://qsfj.com/products/3002)
* [FCC Reports](https://fcc.id/XBPUV-K5) / [fcc.gov](https://apps.fcc.gov/oetcf/eas/reports/ViewExhibitReport.cfm?mode=Exhibits&RequestTimeout=500&calledFromFrame=Y&application_id=8sqkxgC%2F1cYNHF0lGkSAwA%3D%3D&fcc_id=XBPUV-K5)


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
