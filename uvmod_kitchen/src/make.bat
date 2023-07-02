@cls
arm-none-eabi-as -mcpu=cortex-m0 -EL -mthumb -march=armv6 -o %~n1.o %1
arm-none-eabi-ld --entry %2 --section-start=.text=%2 -o %~n1.elf %~n1.o
arm-none-eabi-objcopy -O binary %~n1.elf %~n1_%2.bin
@del %~n1.elf
@del %~n1.o