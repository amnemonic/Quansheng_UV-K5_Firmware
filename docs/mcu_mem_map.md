## Flash
| Start address | End address | Description                   |
| --            |  --         | --                            |
| `0x00000`     | `0x0EFFF`   | Normal operation mode program |
| `0x0F000`     | `0x0FFFF`   | Firmware update mode program  |
| `0x10000`     | `0x107FF`   | Boot code                     |


## RAM 
RAM memory mapped at address `0x20000000`

## Peripherals 

### GPIO - PORT_A
Base address: `0x40060000` <br>
Direction address: `0x40060004` 

Exposed pins
| Pin  | Function   |
|  --: | :--        |
| PA3  |            |
| PA4  |            |
| PA5  |            |
| PA6  |            |
| PA7  |            |
| PA8  |            |
| PA9  | Battery voltage ADC (SARADC_CH04) |
| PA10 | I2C_SCL for EEPROM and BK1080 |
| PA11 | I2C_SDA for EEPROM and BK1080 |
| PA12 |            |
| PA13 |            |
| PA14 | Unknown Analog value (SARADC_CH09) |





### GPIO - PORT_B
Base address: `0x40060800` <br>
Direction address: `0x40060804`

Exposed pins
| Pin  | Function         |
|  --: | :--              |
| PB6  | LCD Backgliht on |
| PB7  |                  |
| PB8  |                  |
| PB9  | ST7565 A0 pin?   |
| PB10 |                  |
| PB11 |                  |
| PB14 |                  |
| PB15 | BK1080 Power on? |




### GPIO - PORT_C
Base address: `0x40061000` <br>
Direction address: `0x40061004`

Exposed pins
| Pin  | Function       |
|  --: | :--            |
| PC0  |                |
| PC1  |                |
| PC2  |                |
| PC3  | Flashlight LED |
| PC4  |                |
| PC5  |                |


### UART
Uart base address: `0x4006B800`




