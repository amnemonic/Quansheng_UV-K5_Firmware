#!/bin/bash

rm -rf temp 2>/dev/null
mkdir temp

python3 qsfirm.py unpack k5_v2.01.26_publish.bin temp/fw.dec.bin temp/fw.ver.bin

# here comment or uncomment mods

python3 mod_enable_swd_port.py    temp/fw.dec.bin
python3 mod_custom_freq_ranges.py temp/fw.dec.bin
python3 mod_remove_tx_limits.py   temp/fw.dec.bin
python3 mod_universal_version.py  temp/fw.ver.bin

# end of mods

python3 qsfirm.py pack temp/fw.dec.bin temp/fw.ver.bin k5_v2.01.26_MODDED.bin
