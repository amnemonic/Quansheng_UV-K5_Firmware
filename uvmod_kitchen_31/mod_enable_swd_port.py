# nothing to configure here

# enables SWD port which is normally disabled during Firwmware startup
# thanks for https://github.com/manujedi

##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct

PORTCONF1_FW_LOC = 0xB994  #v2.01.31
PORTCONF2_FW_LOC = 0xBA22  #v2.01.31


print('\n>>> Running',os.path.basename(sys.argv[0]),'mod...')
fw =  bytearray(open(sys.argv[1],'rb').read())


fw[PORTCONF1_FW_LOC:PORTCONF1_FW_LOC+2] = b'\x00\xBF'  if fw[PORTCONF1_FW_LOC:PORTCONF1_FW_LOC+2] == b'\xC8\x60'  else print('Function not found @PORTCONF1_FW_LOC. Wrong FW version or already patched')
fw[PORTCONF2_FW_LOC:PORTCONF2_FW_LOC+2] = b'\x00\xBF'  if fw[PORTCONF2_FW_LOC:PORTCONF2_FW_LOC+2] == b'\x48\x60'  else print('Function not found @PORTCONF2_FW_LOC. Wrong FW version or already patched')

if fw[PORTCONF1_FW_LOC:PORTCONF1_FW_LOC+2] == b'\x00\xBF' and fw[PORTCONF2_FW_LOC:PORTCONF2_FW_LOC+2] == b'\x00\xBF': print('SWD port enabled successfully')


open(sys.argv[1],'wb').write(fw)
