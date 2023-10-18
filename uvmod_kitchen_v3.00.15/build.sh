#!/bin/bash

rm -rf temp 2>/dev/null
mkdir temp

python3 qsfirm.py unpack K6_V3.00.15.bin temp/fw.dec.bin temp/fw.ver.bin

# here comment or uncomment mods

python3 mod_custom_freq_ranges.py temp/fw.dec.bin
python3 mod_remove_tx_limits.py   temp/fw.dec.bin
python3 mod_universal_version.py  temp/fw.ver.bin
python3 mod_battery_icon.py temp/fw.dec.bin
python3 mod_increases_abr_values.py temp/fw.dec.bin
python3 mod_custom_steps.py temp/fw.dec.bin

# end of mods

python3 qsfirm.py pack temp/fw.dec.bin temp/fw.ver.bin K6_V3.00.15-MODDED.bin
