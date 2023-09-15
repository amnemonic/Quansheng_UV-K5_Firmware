# choose the replacement strings for all of the menu options
# each entry follows the pattern of {address, name, size, string}, where string is what you want to edit and size is the maximum characters allowed

addr = 0xDD21

strings = [
    # menu strings
    (addr+7*0 , 'squelch'                         , 6, 'SQL'   ),
    (addr+7*1 , 'step'                            , 6, 'STEP'  ),
    (addr+7*2 , 'txpower'                         , 6, 'TXP'   ),
    (addr+7*3 , 'r dcs'                           , 6, 'R_DCS' ),
    (addr+7*4 , 'r ctcs'                          , 6, 'R_CTCS'),
    (addr+7*5 , 't dcs'                           , 6, 'T_DCS' ),
    (addr+7*6 , 't ctcs'                          , 6, 'T_CTCS'),
    (addr+7*7 , 'tx shift direction'              , 6, 'SFT-D' ),
    (addr+7*8 , 'tx shift offset'                 , 6, 'OFFSET'),
    (addr+7*9 , 'wide/narrow'                     , 6, 'W/N'   ),
    (addr+7*10, 'scramble'                        , 6, 'SCR'   ),
    (addr+7*11, 'busy channel ptt lock'           , 6, 'BCL'   ),
    (addr+7*12, 'save channel'                    , 6, 'MEM-CH'),
    (addr+7*13, 'battery saver'                   , 6, 'SAVE'  ),
    (addr+7*14, 'voice activated mode'            , 6, 'VOX'   ),
    (addr+7*15, 'backlight timeout'               , 6, 'ABR'   ),
    (addr+7*16, 'dual watch'                      , 6, 'TDR'   ),
    (addr+7*17, 'cross band mode'                 , 6, 'WX'    ),
    (addr+7*18, 'key beep'                        , 6, 'BEEP'  ),
    (addr+7*19, 'tx timeout'                      , 6, 'TOT'   ),
    (addr+7*20, 'voice prompt'                    , 6, 'VOICE' ),
    (addr+7*21, 'scan mode'                       , 6, 'SC-REV'),
    (addr+7*22, 'channel display mode'            , 6, 'MDF'   ),
    (addr+7*23, 'auto keypad lock'                , 6, 'AUTOLK'),
    (addr+7*24, 'ch in scan list 1'               , 6, 'S-ADD1'),
    (addr+7*25, 'ch in scan list 2'               , 6, 'S-ADD2'),
    (addr+7*26, 'tail tone elimination'           , 6, 'STE'   ),
    (addr+7*27, 'repeater tail tone elimination'  , 6, 'RP-STE'),
    (addr+7*28, 'mic sensitivity'                 , 6, 'MIC'   ),
    (addr+7*29, 'one key call channel'            , 6, '1-CALL'),
    (addr+7*30, 'active scan list'                , 6, 'S-LIST'),
    (addr+7*31, 'browse scan list 1'              , 6, 'SLIST1'),
    (addr+7*32, 'browse scan list 2'              , 6, 'SLIST2'),
    (addr+7*33, 'alarm mode'                      , 6, 'AL-MOD'),
    (addr+7*34, 'dtmf radio id'                   , 6, 'ANI-ID'),
    (addr+7*35, 'dtmf upcode'                     , 6, 'UPCODE'),
    (addr+7*36, 'dtmf downcode'                   , 6, 'DWCODE'),
    (addr+7*37, 'dtmf using keypad while ptt'     , 6, 'D-ST'  ),
    (addr+7*38, 'dtmf response mode'              , 6, 'D-RSP' ),
    (addr+7*39, 'dtmf hold time'                  , 6, 'D-HOLD'),
    (addr+7*40, 'dtmf pre-load time'              , 6, 'D-PRE' ),
    (addr+7*41, 'dtmf transmit id on ptt'         , 6, 'PTT-ID'),
    (addr+7*42, 'dtmf only listen to contacts'    , 6, 'D-DCD' ),
    (addr+7*43, 'dtmf list/call contacts'         , 6, 'D-LIST'),
    (addr+7*44, 'power on screen'                 , 6, 'PONMSG'),
    (addr+7*45, 'end of talk tone'                , 6, 'ROGER' ),
    (addr+7*46, 'battery voltage'                 , 6, 'VOL'   ),
    (addr+7*47, 'enable AM reception on AM bands' , 6, 'AM'    ),
    (addr+7*48, 'enable NOAA scan'                , 6, 'NOAA_S'),
    (addr+7*49, 'delete channel'                  , 6, 'DEL-CH'),
    (addr+7*50, 'reset radio'                     , 6, 'RESET' ),
    (addr+7*51, 'enable tx on 350mhz band'        , 6, '350TX' ), # the menu entries below are only visible when powering the radio up while holding PTT and side key 1 
    (addr+7*52, 'limit to local ham frequencies'  , 6, 'F-LOCK'),
    (addr+7*53, 'enable tx on 200mhz band'        , 6, '200TX' ),
    (addr+7*54, 'enable tx on 500mhz band'        , 6, '500TX' ),
    (addr+7*55, 'enable 350mhz band'              , 6, '350EN' ),
    (addr+7*56, 'enable scrambler option'         , 6, 'SCREN' ),

    # option strings
    (addr + 399, 'battery saver: off'              , 3, 'OFF'   ),
    (addr + 403, 'battery saver: 1:1'              , 3, '1:1'   ),
    (addr + 407, 'battery saver: 1:2'              , 3, '1:2'   ),
    (addr + 411, 'battery saver: 1:3'              , 3, '1:3'   ),
    (addr + 415, 'battery saver: 1:4'              , 3, '1:4'   ),
    (addr + 419, 'tx power: low'                   , 4, 'LOW'   ),
    (addr + 424, 'tx power: mid'                   , 4, 'MID'   ),
    (addr + 429, 'tx power: high'                  , 4, 'HIGH'  ),
    (addr + 434, 'bandwidth: wide'                 , 6, 'WIDE'  ),
    (addr + 441, 'bandwidth: narrow'               , 6, 'NARROW'),
    (addr + 448, 'multiple options 1: off'         , 6, 'OFF'   ),
    (addr + 455, 'multiple options 1: chan a'      , 6, 'CHAN_A'),
    (addr + 462, 'multiple options 1: chan b'      , 6, 'CHAN_B'),
    (addr + 469, 'multiple options 2: off'         , 3, 'OFF'   ),
    (addr + 473, 'multiple options 2: on'          , 3, 'ON'    ),
    (addr + 477, 'voice prompt: off'               , 3, 'OFF'   ),
    (addr + 481, 'voice prompt: chinese'           , 3, 'CHI'   ),
    (addr + 485, 'voice prompt: english'           , 3, 'ENG'   ),
    (addr + 489, 'dtmf ptt id: off'                , 4, 'OFF'   ),
    (addr + 494, 'dtmf ptt id: upcode on ptt'      , 4, 'BOT'   ),
    (addr + 499, 'dtmf ptt id: downcode after ptt' , 4, 'EOT'   ),
    (addr + 504, 'dtmf ptt id: both'               , 4, 'BOTH'  ),
    (addr + 509, 'scan mode: continue after 5s'    , 2, 'TO'    ),
    (addr + 512, 'scan mode: stay while signal'    , 2, 'CO'    ),
    (addr + 515, 'scan mode: stop on signal'       , 2, 'SE'    ),
    (addr + 518, 'channel display mode: freq'      , 4, 'FREQ'  ),
    (addr + 523, 'channel display mode: chan'      , 4, 'CHAN'  ),
    (addr + 528, 'channel display mode: name'      , 4, 'NAME'  ),
    (addr + 533, 'tx shift direction: off'         , 4, 'OFF'   ),
    (addr + 537, 'tx shift direction: +'           , 4, '+'     ),
    (addr + 541, 'tx shift direction: -'           , 4, '-'     ),
    (addr + 545, 'alarm mode: local'               , 4, 'SITE'  ),
    (addr + 550, 'alarm mode: local + remote'      , 4, 'TONE'  ),
    (addr + 555, 'power on screen: full'           , 4, 'FULL'  ),
    (addr + 560, 'power on screen: custom message' , 4, 'MSG'   ),
    (addr + 565, 'power on screen: batt voltage'   , 4, 'VOL'   ),
    (addr + 570, 'reset: keep channel parameters'  , 3, 'VFO'   ),
    (addr + 574, 'reset: reset everything'         , 3, 'ALL'   ),
    (addr + 578, 'dtmf response: nothing'          , 5, 'NULL'  ),
    (addr + 584, 'dtmf response: local ring'       , 5, 'RING'  ),
    (addr + 590, 'dtmf response: auto call back'   , 5, 'REPLY' ),
    (addr + 596, 'dtmf response: ring and call'    , 5, 'BOTH'  ),
    (addr + 602, 'end of talk tone: off'           , 5, 'OFF'   ),
    (addr + 608, 'end of talk tone: classic beep'  , 5, 'ROGER' ),
    (addr + 614, 'end of talk tone: MDC ID sound'  , 5, 'MDC'   ),
    (addr + 620, 'f lock: none'                    , 3, 'OFF'   ),
    (addr + 624, 'f lock: region FCC'              , 3, 'FCC'   ),
    (addr + 628, 'f lock: region Europe'           , 3, 'CE'    ),
    (addr + 632, 'f lock: region GB'               , 3, 'GB'    ),
    (addr + 636, 'f lock: 430 band'                , 3, '430'   ),
    (addr + 640, 'f lock: 438 band'                , 3, '438'   ),
]


##--------------------- do not modify below this line ---------------------------------------------------
import os,sys

print('Running', os.path.basename(sys.argv[0]), 'mod...')

fw = bytearray(open(sys.argv[1], 'rb').read())

for address, description, size, string in strings:
    if (fw[address:address+size].decode('ascii').rstrip('\x00') != string.rstrip('\x00')): # only patch strings that are different from the original firmware
        
        print('Patching string: ', description)
        print('╰───', fw[address:address+size].decode('ascii'), ' ──▻ ', string)

        if(len(string) > size):
            raise ValueError(f"String '{string}' is longer than allowed size {size}")
        
        fw[address:address+size] = string.ljust(size, '\x00').encode()

open(sys.argv[1], 'wb').write(fw)
