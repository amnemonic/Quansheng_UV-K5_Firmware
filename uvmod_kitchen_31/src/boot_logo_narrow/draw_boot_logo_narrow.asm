.syntax unified
.thumb
.arch armv6-m
.align 1
.code 16

.include "uvk5_v31_symbols.asm"


@@@ ->>>> 0x9BAC
.text
    PUSH    {R4,R5,LR}
    
    MOVS    R2, #0x55                @fillchar
    LDR     R1, =LCD_BUFFER_SIZE     @length
    LDR     R0, =LCD_BUFFER_START    @address
    BL      fillmemory
    
    _copymem 0xAAAAAAAA, 0xBBBBBBBB, 0xCCCCCCCC

    BL      drawStatusBar
    BL      drawMainScreen

    POP     {R4,R5,PC}

