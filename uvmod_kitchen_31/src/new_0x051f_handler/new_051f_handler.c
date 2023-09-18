#include "ver26.h"

//#define DEBUG

int main()
{
    unsigned short request_type = *(unsigned short*)(UART_CMD_BUFFER+4);
    int request_arg1 = *(int*)(UART_CMD_BUFFER+6);
    int request_arg2 = *(int*)(UART_CMD_BUFFER+10);
    int request_arg3 = *(int*)(UART_CMD_BUFFER+14);
    
#ifdef DEBUG
    char buffer[40];
    FormatString(buffer, "Request type = %u; ", request_type);
    uart_sendData(buffer,strlen(buffer));
    
    FormatString(buffer, "Argumens = %u %u %u; ", request_arg1,request_arg2, request_arg3);
    uart_sendData(buffer,strlen(buffer));
#else
    if (request_type==1) {
        uart_sendData((char *)request_arg1,request_arg2);
    } else {
        uart_sendData("Unkn req",8);
    }
#endif

    return 0;
}
