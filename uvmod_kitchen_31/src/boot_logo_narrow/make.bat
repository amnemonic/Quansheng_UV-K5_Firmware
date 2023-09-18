@echo off
color 0e
set PATH=D:\ARM_DEVEL\gcc-arm-none-eabi-10.3-2021.10\bin;%PATH%
set PATH=D:\ARM_DEVEL\gcc-arm-none-eabi-10.3-2021.10\arm-none-eabi\bin;%PATH%
set PATH=%cd%;%PATH%
cls

set in_file=draw_boot_logo_narrow
set baseaddr=0x9BAC


arm-none-eabi-as -mcpu=cortex-m0 -EL -mthumb -march=armv6 -o %in_file%.o %in_file%.asm
arm-none-eabi-ld --entry %baseaddr% --section-start=.text=%baseaddr% -o %in_file%.elf %in_file%.o
arm-none-eabi-objcopy -O binary %in_file%.elf %in_file%_%baseaddr%.bin
del %in_file%.elf
del %in_file%.o


..\bin2py.py %in_file%_%baseaddr%.bin

