@echo off
@rmdir /q /s temp 2>NUL
@mkdir temp

@echo Extracting firmare...
python qsfirm.py unpack k5_v2.01.31_publish.bin temp\fw.dec.bin temp\fw.ver.bin

:: here comment or uncomment mods

python mod_enable_swd_port.py        temp\fw.dec.bin
python mod_custom_freq_ranges.py     temp\fw.dec.bin
python mod_remove_tx_limits.py       temp\fw.dec.bin
python mod_enable_am_everywhere.py   temp\fw.dec.bin
python mod_universal_version.py      temp\fw.ver.bin

:: end of mods

@echo Repacking firmware...
python qsfirm.py pack temp\fw.dec.bin temp\fw.ver.bin k5_v2.01.31_MODDED.bin

