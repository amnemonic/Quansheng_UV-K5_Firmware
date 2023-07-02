/* useful functions */
.equ copymem        , 0x0178
.equ drawStatusBar  , 0xB6B0
.equ drawMainScreen , 0xB638



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
