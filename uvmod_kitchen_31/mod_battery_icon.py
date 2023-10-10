# the original battery icon looks stupid, with the bars starting on the left and the odd line art. this replaces it with a more familiar design. 
# the two offsets used in fw[0xD3BC+134:0xD3BC+223] limit the data to just the battery bitmaps, while fw[0xD3BC:0xD3BC] contains the entire set of 8px symbols for future mods


##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct
print('Running',os.path.basename(sys.argv[0]),'mod...')

fw =  bytearray(open(sys.argv[1],'rb').read())
if fw[0xD3BC+134:0xD3BC+223] == b'>"\x7fAAAAAAAAAAAAAc\x00>"\x7fA]]AAAAAAAAAAc\x00>"\x7fA]]A]]AAAAAAAc\x00>"\x7fA]]A]]A]]AAAAc\x00>"\x7fA]]A]]A]]A]]Ac': 
    print('Patching battery icon data...')
    fw[0xD3BC+134:0xD3BC+223] = b'>"cAAAAAAAAAAAAA\x7f\x00>"cAAAAAAAAAA]]Ac\x00>"cAAAAAAA]]A]]A\x7f\x00>"cAAAA]]A]]A]]A\x7f\x00>"cA]]A]]A]]A]]A\x7f'
else:
    print('ERROR: Cant find data')
    sys.exit(0)


open(sys.argv[1],'wb').write(fw)
