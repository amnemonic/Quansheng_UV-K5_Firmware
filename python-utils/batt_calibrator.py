import libuvk5
import sys,os
import struct

if len(sys.argv)<3: print(f'Usage: {os.path.basename(sys.argv[0])} <COMx> <read | write  val0 val1 val2 val3 val4 val5 | calibrate>') ; exit(1)
arg_port = sys.argv[1]
action   = sys.argv[2]

with libuvk5.uvk5(arg_port) as radio:
    radio.debug=False
    if radio.connect():
        _=radio.get_fw_version() #mandatory before reading mem
        calib_raw = radio.get_cfg_mem(0x1F40,16)
        calib_data     = list(struct.unpack('<8H',calib_raw))
        calib_data_old = [i for i in calib_data]
        if action=='read':
            print(calib_data[0:6])

        if action=='write': 
            if len(sys.argv)!=9: print(f'Usage: {os.path.basename(sys.argv[0])} <COMx> write val0 val1 val2 val3 val4 val5') ; exit(1)
            calib_data[0] = int(sys.argv[3],0)
            calib_data[1] = int(sys.argv[4],0)
            calib_data[2] = int(sys.argv[5],0)
            calib_data[3] = int(sys.argv[6],0)
            calib_data[4] = int(sys.argv[7],0)
            calib_data[5] = int(sys.argv[8],0)
            calib_raw = struct.pack('<8H',*calib_data)
            radio.set_cfg_mem(0x1F40,calib_raw)

        if action=='calibrate':
            while True:
                actual_voltage = input("Enter voltage from multimeter and press enter: ")
                try:
                    actual_voltage = float(actual_voltage.replace(',','.'))
                except:
                    actual_voltage = None
                    
                if actual_voltage is not None:
                    break
            adc_value = radio.get_adc()[0]
            new_coeff = int(760*adc_value/actual_voltage/100)
            print('Current battery voltage         = {:.2f}'.format(760*adc_value/calib_data[3]/100))
            print('Current battery ADC coefficient = {}'.format(calib_data[3]))
            print('')
            print('Desired battery voltage         = {:.2f}'.format(actual_voltage))
            print('New battery ADC coefficient     = {}'.format(new_coeff))
            print('Wait... ', end='')
            calib_data[3] = new_coeff
            calib_raw = struct.pack('<8H',*calib_data)
            radio.set_cfg_mem(0x1F40,calib_raw)
            print('OK. New value written to eeprom')
            print('Previous calibration values:',calib_data_old[0:6])            
            print('Current calibration values :',struct.unpack('<8H',radio.get_cfg_mem(0x1F40,16))[0:6])
            print('')
            print('!!! PLEASE REBOOT RADIO FOR THE CHANGES TO TAKE EFFECT !!!')
