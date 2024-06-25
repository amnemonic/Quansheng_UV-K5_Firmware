@echo off
@rmdir /q /s temp 2>NUL
@mkdir temp

@echo Extracting firmare...
python qsfirm.py unpack k5_v2.01.26_publish.bin temp\fw.dec.bin temp\fw.ver.bin



:: mods by https://github.com/piotr022
:: please choose only one of them and always 
:: place as first mod in this batch file
rem mod_piotr022_rssi_sbar.py temp\fw.dec.bin
rem mod_piotr022_rssi_printer.py temp\fw.dec.bin



:: here comment or uncomment mods
    python mod_battery_icon.py temp\fw.dec.bin
rem python mod_negative_screen.py temp\fw.dec.bin
rem python mod_change_contrast.py temp\fw.dec.bin
rem python mod_mic_gain.py temp\fw.dec.bin

rem python mod_custom_font.py temp\fw.dec.bin
rem python mod_custom_font_DO7OO.py temp\fw.dec.bin
rem python mod_custom_font_VCR.py temp\fw.dec.bin
rem python mod_custom_font_comicsans.py temp\fw.dec.bin

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

rem python src\new_0x051f_handler\mod_051f_ramreader.py temp\fw.dec.bin
rem python mod_roger_mototrbo_like.py temp\fw.dec.bin
rem python mod_universal_version.py temp\fw.ver.bin

:: end of mods

@echo Repacking firmware...
python qsfirm.py pack temp\fw.dec.bin temp\fw.ver.bin k5_v2.01.26_MODDED.bin

