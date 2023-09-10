## Create your own custom rom for Quansheng UV-K5!

### Prerequisites 
 - Windows
 - [Latest python](https://www.python.org/downloads/) installed

### How to use this?
 - customize included mods, for example `mod_custom_freq_ranges.py` has possibility to edit frequency ranges
 - edit `build.bat`/`build.sh`, if you want omit execution of any mod, prefix its line with `::` or `rem` (`#` in `build.sh`)
 - [start command prompt](https://www.google.com/search?q=how+to+open+command+prompt+windows) in `uvmod_kitchen_31` directory
 - run command `build.bat`/`build.sh`
 - look for any errors
 - now you can flash new firmware file named `k5_v2.01.31_MODDED.bin`

## List of mods
Porting most useful mods from v26 to v31, for now below mods are ported:
 - `mod_custom_freq_ranges.py` - customize frequency ranges F1 - F7
 - `mod_enable_swd_port.py` - enables debug port during normal radio operation
 - `mod_remove_tx_limits.py` - completely removes transmit limits
 - `mod_universal_version.py` - allow to flash output firmware also on `UV-K6` and `UV-5R PLUS`
 - `mod_enable_am_everywhere.py` - allow to change modulation on all frequency ranges F1 - F7

