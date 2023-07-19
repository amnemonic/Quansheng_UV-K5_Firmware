#!/bin/bash

rm -rf temp 2>/dev/null
mkdir temp

python3 qsfirm.py unpack k5_v2.01.26_publish.bin temp/fw.dec.bin temp/fw.ver.bin

# here comment or uncomment mods
  mod_battery_icon.py temp/fw.dec.bin
# mod_negative_screen.py temp/fw.dec.bin
# mod_change_contrast.py temp/fw.dec.bin
# mod_mic_gain.py temp/fw.dec.bin

# mod_custom_font.py temp/fw.dec.bin
# mod_custom_font_DO7OO.py temp/fw.dec.bin
# mod_custom_font_VCR.py temp/fw.dec.bin

  mod_custom_freq_ranges.py temp/fw.dec.bin
# mod_custom_noaa_freqs.py temp/fw.dec.bin

# mod_custom_steps.py temp/fw.dec.bin
  mod_more_freq_steps_and_backlight_duration.py temp/fw.dec.bin

# mod_disable_tx_completely.py temp/fw.dec.bin
# mod_enable_tx_50to850.py temp/fw.dec.bin
# mod_enable_tx_50to850_except_airband.py temp/fw.dec.bin
# mod_enable_swd_port.py temp/fw.dec.bin

# mod_menu_strings.py temp/fw.dec.bin

# .\src\new_0x051f_handler\mod_051f_ramreader.py temp\fw.dec.bin

python3 qsfirm.py pack temp/fw.dec.bin temp/fw.ver.bin k5_v2.01.26_MODDED.bin
