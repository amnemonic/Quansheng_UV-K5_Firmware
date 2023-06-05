@rmdir /q /s temp 2>NUL
@mkdir temp

qsfirm.py unpack k5_v2.01.26_publish.bin temp\fw.dec.bin temp\fw.ver.bin

:: here comment or uncomment mods
mod_custom_steps.py temp\fw.dec.bin
mod_custom_freq_ranges.py temp\fw.dec.bin


qsfirm.py pack temp\fw.dec.bin temp\fw.ver.bin k5_v2.01.26_MODDED.bin

