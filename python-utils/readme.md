## Various utility scripts useful when modding / reversing firmware. 
All scripts uses my library `libuvk5.py`. Scripts tested only on windows.
<hr>

## To read write access COM Port (Serial/USB Cable) must be the Serial Module installed into Python.

Install from command prompt/cmd the serial module for Python and run: 
```
py -m pip install serial
```
Python download the module and it's available in your environment (Windows,...)
<hr>

### `fw_unpack.py`
Usage sample:
```
fw_unpack.py k5_v2.01.19_publish.bin
```
Sample output:
```
CRC OK
Saved decoded firmware to k5_v2.01.19_publish.dec.bin
Saved version info to k5_v2.01.19_publish.ver.bin
```
Description:<br>
Scripts checks file's CRC then decode it and creates two new files with suffix `.dec.bin` and `.ver.bin`. If you just want to revere engineer file then only first file is needed. Second one is used by next script `fw_pack.py` to put together file ready to upload to device.
<hr>



### `fw_pack.py`
Usage sample:
```
fw_pack.py k5_v2.01.19_publish.dec.bin k5_v2.01.19_publish.ver.bin k5_v2.01.19_reassembled.bin
```
Sample output:
```
Saved encoded firmware to k5_v2.01.19_reassembled.bin
```
Description:<br>
It creates encoded file with correct CRC and version bytes inserted in file. Ready for use with orginal updater. 
<hr>


### `configmem_read.py`
Arguments:
```
configmem_read.py <COMx> <address> <len>
```
Usage sample:
```
configmem_read.py COM4 0x0F40 8
```
Sample output:
```
00010001010101ff
```
Description:<br>
Script reads contents of configuration memory directly to console. 
<hr>




### `configmem_write.py`
Arguments:
```
configmem_write.py <COMx> <address> <hex_payload>
```
Usage sample:
```
configmem_write.py COM4 0x0F40 00010001010101ff
```
Sample output:
```
PAYLOAD= 00010001010101ff
```
Description:<br>
Script writes bytes given in payload directly to device. **Payload has to be multiply of 8 bytes**
<hr>



### `reboot_radio.py`
Arguments:
```
reboot_radio.py <COMx>
```
Usage sample:
```
reboot_radio.py COM4
```
Description:<br>
Script just reboots device. Command not produce any output in normal situation. Usefull for example after using `configmem_write.py`
<hr>


### `batt_calibrator.py`
Arguments:
```
batt_calibrator.py <COMx> <read | write  val0 val1 val2 val3 val4 val5 | calibrate>
```

To calibrate ADC so battery voltage display more accurately invoke `batt_calibrator.py COM1 calibrate` like below:
```
> batt_calibrator.py COM1 calibrate
Enter voltage from multimeter and press enter:
```
now follow steps: 
- connect radio to PC
- power on radio
- lay your radio with display to the bottom and battery up
- measure voltage on two exposed pad on bottom of the battery
- wait till voltage stabilizes
- write measuder voltage in format `1.23` or `1,23` it shoudl not matter
- hit enter
- reboot radio

You can backup current calibration values by starting `batt_calibrator.py COM1 read`

To read more about values and its meaning please refer to [documentation](https://github.com/amnemonic/Quansheng_UV-K5_Firmware/blob/main/docs/cfg_mem_map.md#battery-calibration-area).
