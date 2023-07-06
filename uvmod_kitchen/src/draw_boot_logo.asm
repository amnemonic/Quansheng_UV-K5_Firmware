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

.include "inc/uvk5_v26_symbols.asm"


@@@ ->>>> 0x9B3C
.text
    PUSH    {R4,R5,LR}
    _copymem LCD_BUFFER_START, 0xDEADBEEF, LCD_BUFFER_SIZE

    BL      drawStatusBar
    BL      drawMainScreen

    POP     {R4,R5,PC}

