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
 - now you can flash new firmware file named `K6_V3.00.15-MODDED.bin`

## List of mods
Porting most useful mods from v2.01.31 to v3.00.15, for now below mods are ported:
 - `mod_custom_freq_ranges.py` - customize frequency ranges F1 - F7
 - `mod_remove_tx_limits.py` - completely removes transmit limits
 - `mod_universal_version.py` - allow to flash output firmware also on `UV-K6` and `UV-5R PLUS`
 - `mod_battery_icon.py` - fix original stupid battery icon
 - `mod_increases_abr_values.py` - increase the value of the ABR by factor 2, 4 or 8 
 - `mod_remove_tx_limits.py` - remove TX LImits

