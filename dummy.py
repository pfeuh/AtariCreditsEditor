#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

print hex(36864), hex(36864+255)

raw_text = """Location      Contents                            Pointers
            +-------------------------------------------------------------+
65535 _____ | Top of memory _____________________________________________ |
            | Operating System ROM                                        |
            |                                                             |
60906-65535 | Device handler routines             794-831 HATABS          |
59716-60905 | Serial Input/Output (SIO) utilities                         |
59093-59715 | Interrupt handler                   512,513 VDSLST          |
            |                                     514-527 Vectors         |
58534-59092 | Central Input/Output (CIO) utilities                        |
            |                                                             |
            |                                                             |
 58533 ____ | Operating System vectors __________________________________ |
58496-58533 | Initial RAM vectors on powerup                              |
58448-58495 | JMP vectors                                                 |
58432-58447 | Cassette                                                    |
58416-58431 | Printer                                                     |
58400-58415 | Keyboard                                                    |
58384-58399 | Screen                                                      |
58368-58383 | Editor                                                      |
            |                                                             |
            |                                                             |
58367 _____ | ROM Character set _________________ 756 CHBAS _____________ |
            |                                                             |
            |                                                             |
57344       |                                                             |
            |                                                             |
            |                                                             |
57343 _____ | Floating Point ROM package                                  |
            |                                                             |
            |                                                             |
55295 _____ | I/O chips _________________________________________________ |
            |                                                             |
            |                                                             |
54784-55295 | Unused                                                      |
54272-54783 | ANTIC                               756     CHBAS           |
            |                                     755     CH1             |
            |                                     564-565 LPEN            |
            |                                     560-561 SDLSTL          |
            |                                     559     SDMCTL          |
54016-54271 | PIA                                 636-639 PTRIG#          |
            |                                     632-635 STICK#          |
53760-54015 | POKEY                               624-631 PADDL#          |
            |                                     562     SSKCTL          |
            |                                     16      POKMSK          |
53504-53759 | unused                                                      |
53248-53503 | GTIA or CTIA                        704-707 PCOLR#          |
            |                                     708-712 COLOR#          |
            |                                     644-647 STRIG#          |
            |                                     623 GPRIOR              |
            |                                                             |
            |                                                             |
53247 _____ | Unused 4K ROM block _______________________________________ |
            |                                                             |
            |                                                             |
49151 _____ | 8K BASIC ROM                                                |
            | or Left cartridge (A)                                       |
            |                                                             |
            |                                                             |
40959 _____ | Top of BASIC RAM or                 106     RAMTOP          |
____________|_____________________________________________________________|
            |                                     740     RAMSIZ          |
            |                                                             |
            | Right cartridge (B) ROM if present                          |
            | (Atari 800 only)                                            |
            |                                                             |
            |                                                             |
Size and    |                                                             |
location    |                                                             |
vary with   |                                                             |
GRAPHICS    |                                                             |
mode        |                                                             |
            | Text window screen RAM              60,661 TXTMSC           |
            | 40800 for GR.0                                              |
            |                                                             |
            | Bottom of screen RAM                88,89   SAVMSC          |
            | 40000 for GR.0                                              |
            |                                                             |
            | Display List:                       560,561 SDLSTL          |
            | 39968 for GR.0                                              |
            |                                                             |
            | Top of BASIC RAM                    741,742 MEMTOP          |
(OS)        |                                                             |
            |                                                             |
            |                                                             |
            |                                                             |
32768       |                                                             |
            |                                                             |
            |                                                             |
32767 _____ | User-program RAM __________________________________________ |
            |                                                             |
            | The amount of RAM can be ascertained by:                    |
            | PRINT FRE(0)                                                |
            |                                                             |
            | Bottom varies: see note below                               |
(13062)     | Depends on buffer area allocated.                           |
            |                                                             |
            |                                                             |
            | RAM used by DOS and File System Manager                     |
            |                                                             |
            |                                     144,145 MEMTOP          |
            | Stack for FOR-NEXT & GOSUB          142,143 RUNSTK          |
            |                                     14,15 APPMHI            |
Size and    |                                                             |
location    |                                                             |
vary with   |                                                             |
program     |                                                             |
size        |                                                             |
            | String & array table &                                      |
            | end of BASIC program                140,141 STARP           |
            |                                                             |
            |                                                             |
            | BASIC program                                               |
            | area                                                        |
            |                                                             |
            |                                                             |
            | Statement table:                    136,137 STMTAB          |
            | Beginning of BASIC program                                  |
            | Variable variable table             134,135 VVTP            |
            |                                                             |
            | VNTP + 1                            132,133 VNTD            |
            |                                                             |
            | Variable name table                 130,131 VNTP            |
            |                                                             |
(7420)      | BASIC bottom of memory              743,744 MEMLO           |
            |                                     128,129 LOMEM           |
            |                                                             |
            | Sector buffers                      4921,4937 SABUFL/H      |
6781        | Drive & sector buffers              4905,4913 DBUFA1/H      |
6047        | DOS vector                          10,11  DOSVEC           |
5440        | DUP.SYS start                                               |
            |                                                             |
5377        | VTOC buffer                                                 |
            | DOS initialization                  12,13   DOSINI          |
            | or BASIC RAM without                (743,744 MEMLO)         |
            | DOS resident                        (128,129 LOMEM)         |
            | FMSRAM                                                      |
1792        | DUP.SYS beginning                                           |
            |                                                             |
            |                                                             |
1791 ______ | RAM used by OS and cartridge.                               |
            | (to bottom of RAM)                                          |
            |                                                             |
            | Page six RAM                                                |
            |                                                             |
            |           +-------------------------------------------------+
            | 1535 ____ | RAM used by BASIC _____________________________ |
            |           | (to bottom of RAM)                              |
            |           |                                                 |
            | 1406      | Floating Point RAM                              |
            | 1405      | BASIC RAM                                       |
            |           |                                                 |
            |           |       +-----------------------------------------+
            |           | 1151  | Operating System RAM                    |
            |           |       |                                         |
            |           |       |                                         |
            |           |       | Cassette buffer                         |
            |           |       |                                         |
            |           |       | Printer buffer                          |
            |           |       |                                         |
            |           |       | IOCB's                                  |
            |           |       |                                         |
            |           | 512   |                                         |
            |           |       |  ______________________________________ |
            |           | 511   | Stack                                   |
            |           |       |                                         |
            |           |       |                                         |
            |           |       |                                         |
            |           | 256   |                                         |
            |           |       |  ______________________________________ |
            |           | 255   | BASIC zero page RAM                     |
            |           |       |                                         |
            |           |       | Floating Point pg. 0                    |
            |           |       |                                         |
            |           |       | Assembler Cart. pg. 0                   |
            |           |       |                                         |
            |           |       |                                         |
            |           |       |                                         |
            |           |       |                                         |
            |           | 128   |                                         |
            |           |       |  ______________________________________ |
            |           | 127   | OS page zero RAM                        |
            |           |       |                                         |
            |           |       |                                         |
            |           |       | Zero page IOCB                          |
            |           |       |                                         |
            |           |       |                                         |
            |           | 0     | Bottom of memory                        |
            +-----------+-------+-----------------------------------------+
"""

raw_text = raw_text.replace('\r', '')
lines = raw_text.split('\n')
for line in lines:
    print line


