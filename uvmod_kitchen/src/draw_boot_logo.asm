/*
 *
 *  make draw_boot_logo.asm 0x9B3C
 *
 */

.syntax unified
.thumb
.arch armv6-m
.align 1
.code 16


@@@ ->>>> 0x9B3C
.text
    PUSH    {R4,R5,LR}
    LDR     R2, =0x400        @Length=1024 (128 x 64 bits)
    LDR     R1, =0xDEADBEEF   @Source addres placeholder, later replaced by image data pointer
    LDR     R0, =0x20000684   @Destination = LCD Buffer
    BL      0x0178            @copy mem

    BL      0xB6B0            @Draw_StatusBar_B6B0
    BL      0xB638            @Draw_MainScreen_B638

    POP     {R4,R5,PC}

