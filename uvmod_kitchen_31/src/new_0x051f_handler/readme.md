### Short description

This mod replaces routine which is responsible for reply to command `0x051F` sent by uart. I don't know for what it is so it is not useful for now at least. New function can be used to read any memory area. For example to read screen buffer run these commands:

```
> util_051f_ramreader.py COM14 0x20000684 0x400 screen_buffer.bin
> raw2bmp.py screen_buffer.bin screen_buffer.png
```


last parameter is optional, if you omit it then you will get raw hex data of selected memory area, for example to read current microphone gain value:

```
> util_051f_ramreader.py COM14 0x20000ad6 0x1
18
```

in next version maybe we can add writing to memory address and read/write registers of BK4819.