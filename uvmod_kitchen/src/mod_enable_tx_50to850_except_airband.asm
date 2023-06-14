/*
 * to assemble and link use commands:
 * 
 * arm-none-eabi-as -mcpu=cortex-m0 -EL -mthumb -march=armv6 -o shellcode.o %1
 * arm-none-eabi-ld --entry 0x0 --section-start=.text=0x1804 -o shellcode.elf shellcode.o
 * arm-none-eabi-objcopy -O binary shellcode.elf shellcode.bin
*/

.syntax unified
.thumb
.arch armv6-m
.align 1
.code 16

.text
    PUSH    {R4-R7,LR}
    MOV     R1, R0
    LDR     R1, [R1,#0x14]
    LDR     R1, [R1]            @ r1 = current freq

    LDR     R2,=0x11111111
    CMP     R1,R2
    BLO     allow_tx            @ if freq < 0x11111111 then goto allow_tx

    LDR     R2,=0x22222222
    CMP     R1,R2
    BHS     allow_tx            @ if freq >= 0x22222222 then goto allow_tx


block_tx:
    MOVS    R0, #0
    MVNS    R0, R0   /* R0=-1 */
    B       exit

allow_tx:
    MOVS    R0, #0
    B       exit


exit:
    POP     {R4-R7,PC}
