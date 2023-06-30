<p align="center">
  <img  src="https://raw.githubusercontent.com/amnemonic/Quansheng_UV-K5_Firmware/main/font_and_graphics/encoder/BigDigits_VCR_font.png">
</p>

Very first attempt to automate custom fonts generation. For now only for big digits in very crude and convoluted way. Usage:
```
BigDigits_encode.py BigDigits_VCR_font.png mod_custom_anything.py
```
as a result you should get file `mod_custom_anything.py` which can be used in [uvmod_kitchen](https://github.com/amnemonic/Quansheng_UV-K5_Firmware/blob/main/uvmod_kitchen/)

Requirements: [Pillow](https://pypi.org/project/Pillow/) library

