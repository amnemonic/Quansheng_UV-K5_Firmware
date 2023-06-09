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

### `mod_negative_screen.py`
No customization. You can just disable or enable it in `build.bat`.

Edits initialization routine of ST7565 (LCD controller) to change default LCD mode normal to negative. See example: [negative_lcd.jpg](https://raw.githubusercontent.com/amnemonic/Quansheng_UV-K5_Firmware/main/hardware/negative_lcd.jpg)
<hr>
