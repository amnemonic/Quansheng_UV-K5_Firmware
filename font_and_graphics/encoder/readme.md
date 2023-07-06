Very first attempt to automate custom fonts generation. For now only for big digits in very crude and convoluted way.
Requirements: [Pillow](https://pypi.org/project/Pillow/) library.

<hr>

### BigDigits
<p align="center">
  <img  src="https://raw.githubusercontent.com/amnemonic/Quansheng_UV-K5_Firmware/main/font_and_graphics/encoder/BigDigits_VCR_font.png">
</p>

9 symbols, each of width=13px, height=16px, in firmware version `k5_2.01.26` at offset `0xD502`, 286 bytes in total.

Usage:

```
BigDigits_encode.py BigDigits_VCR_font.png mod_custom_bigdigits.py
```

as a result you should get file `mod_custom_bigdigits.py` which can be used in [uvmod_kitchen](https://github.com/amnemonic/Quansheng_UV-K5_Firmware/blob/main/uvmod_kitchen/)
<hr>

### Alphabet
<p align="center">
  <img  src="https://raw.githubusercontent.com/amnemonic/Quansheng_UV-K5_Firmware/main/font_and_graphics/encoder/Alphabet_Stock_Font.png">
</p>

95 symbols, each of width=8px, height=16px, in firmware version `k5_2.01.26` at offset `0xD66D`, 1520 bytes in total.

Usage:
```
Alphabet_encode.py Alphabet_Stock_Font.png mod_custom_alphabet.py
```

as a result you should get file `mod_custom_alphabet.py` which can be used in [uvmod_kitchen](https://github.com/amnemonic/Quansheng_UV-K5_Firmware/blob/main/uvmod_kitchen/)
<hr>

### symbols
<p align="center">
  <img  src="https://raw.githubusercontent.com/amnemonic/Quansheng_UV-K5_Firmware/main/font_and_graphics/encoder/Symbols_stock.png" width="884" height="16">
</p>

few symbols, various width, height=8px, in firmware version `k5_2.01.26` at offset `0xD348`, 442 bytes in total.

Usage:
```
Symbols_encode.py Symbols_stock.png mod_custom_symbols.py
```

as a result you should get file `mod_custom_symbols.py` which can be used in [uvmod_kitchen](https://github.com/amnemonic/Quansheng_UV-K5_Firmware/blob/main/uvmod_kitchen/)
<hr>