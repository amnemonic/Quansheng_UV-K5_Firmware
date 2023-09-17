#define SCREEN_STATUS_BAR_START 0x20000684
#define SCREEN_STATUS_BAR_LEN   0x80

#define SCREEN_MAINAREA_START   0x20000704
#define SCREEN_MAINAREA_LEN     0x380

#define UART_CMD_BUFFER 0x20000584



#define PrintTextOnScreen        ((  void(*)(const char* U8Text, unsigned int u32StartPixel, unsigned int u32StopPixel, unsigned int u32LineNumber, unsigned int u32PxPerChar, unsigned int u32Centered)  )0x874C + 1)
#define FillScreenMemory         ((  void(*)(unsigned int u32Param1)                                                                                                                                      )0xb70c + 1)
#define DelayMs                  ((  void(*)(unsigned int u32Ms)                                                                                                                                          )0xD0EE + 1)
#define DelayUs                  ((  void(*)(unsigned int u32Us)                                                                                                                                          )0xD100 + 1)
#define uart_sendData            ((  int(*)(char * p8Data, unsigned int u8Len)                                                                                                                            )0xBE44 + 1)
#define BK4819Write              ((  void(*)(unsigned int u32Address, unsigned int u32Data)                                                                                                               )0xAF00 + 1)
#define BK4819Read               ((  unsigned int(*)(unsigned int u32Address)                                                                                                                             )0xA960 + 1)
#define FlushFramebufferToScreen ((  void(*)(void)                                                                                                                                                        )0xB638 + 1)
#define FlushStatusBarToScreen   ((  void(*)(void)                                                                                                                                                        )0xB6B0 + 1)
#define PollKeyboard             ((  unsigned int(*)(void)                                                                                                                                                )0xb0b8 + 1)
#define sprintf                  ((  char* (*)(char *, const char *, ...)                                                                                                                                 )0xc8ec + 1)
#define FillWithZero             ((  void(*)(unsigned char* p8Data, unsigned int u32Size)                                                                                                                 )0x01AA + 1)
#define FormatString             ((  char* (*)(char *, const char *, ...)                                                                                                                                 )0xC6E8 + 1)
#define strlen                   ((  unsigned char(*)(char *)                                                                                                                                             )0x01C0 + 1)
#define memcpy                   ((  void(*)(void *dest, const void *source, size_t size)                                                                                                                 )0x0178 + 1)


