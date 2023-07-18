## Create your own custom rom for Quansheng UV-K5!

### Prerequisites 
 - Windows
 - [Latest python](https://www.python.org/downloads/) installed

### How to use this?
 - customize included mods, for example `mod_custom_freq_ranges.py` has possibility to edit frequency ranges
 - edit `build.bat`, if you want omit execution of any mod, prefix its line with `::` or `rem`
 - [start command prompt](https://www.google.com/search?q=how+to+open+command+prompt+windows) in `uvmod_kitchen` directory
 - run command `build.bat`
 - look for any errors
 - now you can flash new firmware file named `k5_v2.01.26_MODDED.bin` 

## List of mods
(not in any particular order)
<hr>

### `mod_custom_font.py`
Customization:
Replace the `font` variable with the raw binary of a 1-bit, uncompressed bitmap that is interleaved as the firmware expects it (a modification to extract_font.py will be made for this purpose soon.)

Replaces the font bitmap with a custom font of your choosing

https://github.com/amnemonic/Quansheng_UV-K5_Firmware/assets/29899901/27962bd0-b079-4595-9dca-8dee232626ee
<hr>

### `mod_custom_font_DO7OO.py`
Similar as above but this time we are changing digits:

https://github.com/amnemonic/Quansheng_UV-K5_Firmware/assets/29899901/3f15dd8c-ee0e-4579-a9bc-4f6ed42fc853
<hr>

### `mod_custom_font_VCR.py`
Changes only big digits to font [VCR OSD Mono](https://www.dafont.com/vcr-osd-mono.font)

![vcrfont](https://github.com/amnemonic/Quansheng_UV-K5_Firmware/assets/29899901/68694dad-19a9-4904-b878-758315ab4d2a)
<hr>


### `mod_custom_bootscreen.py`
Set up your custom boot logo image. Just like in old times of nokia 3310 😉
By default Q logo is set. To set up your own image paint a b&w bitmap image of size 128x64px then convert it to array using application like [LCD Assistant](http://en.radzio.dxp.pl/bitmap_converter/)

![qs_logo](https://github.com/amnemonic/Quansheng_UV-K5_Firmware/assets/29899901/7fece61e-ee21-47f4-a84d-da23b8c0721d)

<hr>


### `mod_custom_bootscreen_narrow.py`
Basically same as above mod but allows to use smaller logo therefore less space at the end of the file.
By default Do7oo logo is set. To set up your own image paint a b&w bitmap image of width 128px then convert it to array using application like [LCD Assistant](http://en.radzio.dxp.pl/bitmap_converter/)

Customization: before drawing logo, screen buffer is filled with value defined in `clean_pattern` variable. if you set it to `0xFF` then screen will be filled "black", if `0x00` then screen will be clean. 

<hr>



### `mod_change_contrast.py`
Customization:
```python
# configure contrast in range from 0 to 63. Default value is 31
new_contrast = 31
```
Edits initialization routine of ST7565 (LCD controller) to change default LCD contrast
<hr>

### `mod_custom_freq_ranges.py`
The purpose of  this mod is to give ability to user to select which ranges should be covered by each 
frequency range of quansheng radio or if to extend them at all. By default, file contains frequency ranges exactly 
like in stock firmware. 

Customization:
```python
# change below sets to new ones, values are in Hz
new_freq_low_limit =   [50_000_000, 108_000_000, 136_000_000, 174_000_000, 350_000_000, 400_000_000, 470_000_000]
new_freq_high_limit =  [76_000_000, 135_999_900, 173_999_900, 349_999_900, 399_999_900, 469_999_900, 600_000_000]
```

Here you can change low and high limit for each frequency band. 
The underscore `_` symbol is omitted by python interpreter and is added only for better readability.
So for example, if you want to fill the gap between 76 and 108Mhz then in second array change first limit from `76_000_000` to `107_999_990` or 
if you want to extend above 600MHz then change last limit from `600_000_000` to `1300_000_000`. Please keep in mind that different ranges 
are demodulated slightly different inside BK4819 chip, and some ranges have enabled AM demodulation while other don't. 
<hr>

### `mod_custom_steps.py`
Customization:
```python
# change below sets to new ones, values are in Hz
new_freq_steps = [2500, 5000, 6250, 10000, 12500, 25000, 8330]
```
Changes array of frequency steps in menu at position 2
<hr>

### `mod_enable_tx_50to850.py`
No customization. You can just disable or enable it in `build.bat`. The purpose of this mod is to **globally disable/bypass** TX lock. 

ℹ️ This patch alone doesn't extend available frequency ranges. For this use `mod_custom_freq_ranges.py` mod.
<hr>

### `mod_mic_gain.py`
No customization. You can just disable or enable it in `build.bat`. The purpose of this mod is to increase the base mic gain from 0 to 16, thus
making all of the mic gain steps in the menu higher as a result.

A crude before (bottom) and after (top):

![image](https://github.com/amnemonic/Quansheng_UV-K5_Firmware/assets/12097904/9c68fa9e-a3dc-4dfc-9d60-07a4399f87f9)

ℹ️ This patch doesn't extend available mic gain steps (they will still be 0-4.) It just increases the _starting point_ on the mic gain
scale sent to the BK4819 mic sensitivity register.
<hr>

### `mod_negative_screen.py`
No customization. You can just disable or enable it in `build.bat`.

Edits initialization routine of ST7565 (LCD controller) to change default LCD mode normal to negative.

<img src="https://raw.githubusercontent.com/amnemonic/Quansheng_UV-K5_Firmware/main/hardware/negative_lcd.jpg" height="280" />
<hr>




### `mod_more_freq_steps.py`
Customization:
```python
# change below steps to new ones, values are in Hz
# You can add reasonably more steps here

new_freq_steps = [2500, 5000, 6250, 10000, 12500, 25000, 8330, 500000, 10, 1250, 20000]
```
Append new, bigger tablie with frequency steps at the end of firmware thus expanding it, but as far as we are below 0xF000 then we should be fine. Please report any bugs as this is more experimental feature than others above.
<hr>


### `mod_custom_noaa_freqs.py`
Customization:
```python
#first 10 PMR446 channels
new_noaa_table =   [446_006_250, 446_018_750, 446_031_250, 446_043_750, 446_056_250, 446_068_750, 446_081_250, 446_093_750, 446_106_250, 446_118_750,  ]
```
Just sets new values for frequencies in NOAA scan list, nothing less, nothing more. 
<hr>


### `mod_disable_tx_completely.py`
No customization. 

On ALL frequencies radio shows "DISABLED" info and don't transmit at any band.

ℹ️ Please do not use this mod together with `mod_enable_tx_50to850.py`
<hr>



### `mod_enable_tx_50to850_except_airband.py`
Customization:
```python
# set values to block band
block_freq_lo = 118_000_000
block_freq_hi = 137_000_000
```

By default block frequencies between 118 and 137MHz. 


ℹ️ Please do not use this mod together with `mod_enable_tx_50to850.py` or `mod_disable_tx_completely.py`
<hr>


### `mod_ota_qrg.py`
Customization:
```python
AIR_COPY_FREQ_HZ = 433_600_000
```

Default value for copying setting over the air aka "AIR COPY" is 410.025 MHz. You can change that default value using this mod.

![aircopy](https://github.com/amnemonic/Quansheng_UV-K5_Firmware/assets/29899901/fe0b7525-e94d-472e-bcc6-c346e9c71fda)


<hr>
