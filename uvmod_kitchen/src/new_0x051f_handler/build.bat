::-----------------------------------------------------------------
@set origin=0x0D04
@set name=new_051f_handler
::-----------------------------------------------------------------


@set PATH=D:\ARM_DEVEL\gcc-arm-none-eabi-10.3-2021.10\bin;%PATH%


arm-none-eabi-gcc --specs=nosys.specs -Wall -g0 -mlittle-endian -mthumb -mgeneral-regs-only -march=armv6-m -mtune=cortex-m0 ^
 -Os ^
 -c %name%.c -o %name%.o 
arm-none-eabi-ld --entry %origin% --section-start=.text=%origin%  %name%.o -o %name%.elf
arm-none-eabi-objcopy -O binary %name%.elf %name%.bin

..\bin2py.py %name%.bin
