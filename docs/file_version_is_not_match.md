If you try to flash modified firmware on `UV-K6`, `UV-K5(8)` or `UV-5R Plus` with official FW update utility then below error will occur:

![vernotmatch](https://github.com/amnemonic/Quansheng_UV-K5_Firmware/assets/29899901/34234b38-b329-45ab-bd01-afaa237040eb)

It will happens always when trying to "cross-flash" firmware from one radio model to another even the radios are 100% compatible.

To fix this you have (only once) flash firmware which will change your version:
- on `UV-K6` or `UV-K5(8)` flash file: [k5_v2.01.27_flashable_on_v3.bin](https://github.com/amnemonic/Quansheng_UV-K5_Firmware/raw/main/firmware/k5_v2.01.27_flashable_on_v3.bin)
- on `UV-5R Plus` flash file: [k5_v2.01.27_flashable_on_v4.bin](https://github.com/amnemonic/Quansheng_UV-K5_Firmware/raw/main/firmware/k5_v2.01.27_flashable_on_v4.bin)

These are unmodified stock firmware from radio but version information is overwritten d so it will allow to flash it by official firmware update utility. 

