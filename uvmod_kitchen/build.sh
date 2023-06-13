#!/bin/bash

rm -rf temp 2>/dev/null
mkdir temp

python3 qsfirm.py unpack k5_v2.01.26_publish.bin temp/fw.dec.bin temp/fw.ver.bin

# here comment or uncomment mods
python3 mod_enable_tx_50to850.py temp/fw.dec.bin
python3 mod_custom_steps.py temp/fw.dec.bin
python3 mod_custom_freq_ranges.py temp/fw.dec.bin
# python3 mod_negative_screen.py temp/fw.dec.bin
# python3 mod_change_contrast.py temp/fw.dec.bin
# python3 mod_custom_steps.py temp/fw.dec.bin
# python3 mod_custom_noaa_freqs.py temp/fw.dec.bin
# python3 mod_mic_gain.py temp/fw.dec.bin
# python3 mod_disable_tx_completely.py temp/fw.dec.bin

python3 qsfirm.py pack temp/fw.dec.bin temp/fw.ver.bin k5_v2.01.26_MODDED.bin
