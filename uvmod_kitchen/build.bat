@rmdir /q /s temp 2>NUL
@mkdir temp

python qsfirm.py unpack k5_v2.01.26_publish.bin temp\fw.dec.bin temp\fw.ver.bin

:: here comment or uncomment mods
    python mod_battery_icon.py temp\fw.dec.bin
rem python mod_negative_screen.py temp\fw.dec.bin
rem python mod_change_contrast.py temp\fw.dec.bin
rem python mod_mic_gain.py temp\fw.dec.bin

rem python mod_custom_font.py temp\fw.dec.bin
rem python mod_custom_font_DO7OO.py temp\fw.dec.bin
rem python mod_custom_font_VCR.py temp\fw.dec.bin

    python mod_custom_freq_ranges.py temp\fw.dec.bin
rem python mod_custom_noaa_freqs.py temp\fw.dec.bin

rem python mod_custom_steps.py temp\fw.dec.bin
    python mod_more_freq_steps_and_backlight_duration.py temp\fw.dec.bin

rem python mod_disable_tx_completely.py temp\fw.dec.bin
rem python mod_enable_tx_50to850.py temp\fw.dec.bin
rem python mod_enable_tx_50to850_except_airband.py temp\fw.dec.bin

rem python mod_menu_strings.py temp\fw.dec.bin
rem python mod_custom_bootscreen.py temp\fw.dec.bin
rem python mod_enable_swd_port.py temp\fw.dec.bin

:: end of mods

python qsfirm.py pack temp\fw.dec.bin temp\fw.ver.bin k5_v2.01.26_MODDED.bin

