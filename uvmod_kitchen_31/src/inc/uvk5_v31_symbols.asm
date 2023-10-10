/* useful functions */
.equ copymem        , 0x01A0
.equ drawStatusBar  , 0xB720
.equ drawMainScreen , 0xB6A8



/* other addresses */
.equ LCD_BUFFER_START, 0x20000684
.equ LCD_BUFFER_SIZE,  0x400



/* useful macros */
.macro _copymem dst, src, len
    LDR     R2, =\len    @Length
    LDR     R1, =\src    @Source address
    LDR     R0, =\dst    @Destination address
    BL      copymem
.endm
