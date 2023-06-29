# choose the replacement strings for all of the menu options, up to 6 ASCII characters are possible
# each entry follows the pattern of {address, name, string}, where string is what you want to edit

patches = [
    (0xDC96+7*0 , 'squelch'                         , 'SQL'   ),
    (0xDC96+7*1 , 'step'                            , 'STEP'  ),
    (0xDC96+7*2 , 'txpower'                         , 'TXP'   ),
    (0xDC96+7*3 , 'r dcs'                           , 'R_DCS' ),
    (0xDC96+7*4 , 'r ctcs'                          , 'R_CTCS'),
    (0xDC96+7*5 , 't dcs'                           , 'T_DCS' ),
    (0xDC96+7*6 , 't ctcs'                          , 'T_CTCS'),
    (0xDC96+7*7 , 'tx shift direction'              , 'SFT-D' ),
    (0xDC96+7*8 , 'tx shift offset'                 , 'OFFSET'),
    (0xDC96+7*9 , 'wide/narrow'                     , 'W/N'   ),
    (0xDC96+7*10, 'scramble'                        , 'SCR'   ),
    (0xDC96+7*11, 'busy channel ptt lock'           , 'BCL'   ),
    (0xDC96+7*12, 'save channel'                    , 'MEM-CH'),
    (0xDC96+7*13, 'battery saver'                   , 'SAVE'  ),
    (0xDC96+7*14, 'voice activated mode'            , 'VOX'   ),
    (0xDC96+7*15, 'backlight timeout'               , 'ABR'   ),
    (0xDC96+7*16, 'dual watch'                      , 'TDR'   ),
    (0xDC96+7*17, 'cross band mode'                 , 'WX'    ),
    (0xDC96+7*18, 'key beep'                        , 'BEEP'  ),
    (0xDC96+7*19, 'tx timeout'                      , 'TOT'   ),
    (0xDC96+7*20, 'voice prompt'                    , 'VOICE' ),
    (0xDC96+7*21, 'scan mode'                       , 'SC-REV'),
    (0xDC96+7*22, 'channel display mode'            , 'MDF'   ),
    (0xDC96+7*23, 'auto keypad lock'                , 'AUTOLK'),
    (0xDC96+7*24, 'ch in scan list 1'               , 'S-ADD1'),
    (0xDC96+7*25, 'ch in scan list 2'               , 'S-ADD2'),
    (0xDC96+7*26, 'tail tone elimination'           , 'STE'   ),
    (0xDC96+7*27, 'repeater tail tone elimination'  , 'RP-STE'),
    (0xDC96+7*28, 'mic sensitivity'                 , 'MIC'   ),
    (0xDC96+7*29, 'one key call channel'            , '1-CALL'),
    (0xDC96+7*30, 'active scan list'                , 'S-LIST'),
    (0xDC96+7*31, 'browse scan list 1'              , 'SLIST1'),
    (0xDC96+7*32, 'browse scan list 2'              , 'SLIST2'),
    (0xDC96+7*33, 'alarm mode'                      , 'AL-MOD'),
    (0xDC96+7*34, 'dtmf radio id'                   , 'ANI-ID'),
    (0xDC96+7*35, 'dtmf upcode'                     , 'UPCODE'),
    (0xDC96+7*36, 'dtmf downcode'                   , 'DWCODE'),
    (0xDC96+7*37, 'dtmf using keypad while ptt'     , 'D-ST'  ),
    (0xDC96+7*38, 'dtmf response mode'              , 'D-RSP' ),
    (0xDC96+7*39, 'dtmf hold time'                  , 'D-HOLD'),
    (0xDC96+7*40, 'dtmf pre-load time'              , 'D-PRE' ),
    (0xDC96+7*41, 'dtmf transmit id on ptt'         , 'PTT-ID'),
    (0xDC96+7*42, 'dtmf only listen to contacts'    , 'D-DCD' ),
    (0xDC96+7*43, 'dtmf list/call contacts'         , 'D-LIST'),
    (0xDC96+7*44, 'power on screen'                 , 'PONMSG'),
    (0xDC96+7*45, 'end of talk tone'                , 'ROGER' ),
    (0xDC96+7*46, 'battery voltage'                 , 'VOL'   ),
    (0xDC96+7*47, 'enable AM reception on AM bands' , 'AM'    ),
    (0xDC96+7*48, 'enable NOAA scan'                , 'NOAA_S'),
    (0xDC96+7*49, 'delete channel'                  , 'DEL-CH'),
    (0xDC96+7*50, 'reset radio'                     , 'RESET' ),
]
# the strings for the hidden menu can easily be added
# the strings for the menu options can also be added but they are in multiple smaller arrays with different character lengths

##--------------------- do not modify below this line ---------------------------------------------------
import os,sys

print('Running', os.path.basename(sys.argv[0]), 'mod...')

fw = bytearray(open(sys.argv[1], 'rb').read())

for address, description, string in patches:
    print('Patching string: ', description)
    print('╰───', fw[address:address+6].decode('ascii'), ' ──▻ ', string)
    string = string.ljust(6, '\x00')
    fw[address:address+6] = string.encode()

open(sys.argv[1], 'wb').write(fw)