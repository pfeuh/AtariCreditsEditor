#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

SCREENCODE_TO_UNICODE = [
    u' ', u'!', u'"', u'#', u'$', u'%', u'&', u"'", u'(', u')', u'*', u'+', u',', u'-', u'.', u'/', 
    u'0', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9', u':', u';', u'<', u'=', u'>', u'?',
    u'@', u'A', u'B', u'C', u'D', u'E', u'F', u'G', u'H', u'I', u'J', u'K', u'L', u'M', u'N', u'O', 
    u'P', u'Q', u'R', u'S', u'T', u'U', u'V', u'W', u'X', u'Y', u'Z', u'[', u'\\',u']', u'^', u'_', 
    u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', 
    u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', 
    u' ', u'a', u'b', u'c', u'd', u'e', u'f', u'g', u'h', u'i', u'j', u'k', u'l', u'm', u'n', u'o', 
    u'p', u'q', u'r', u's', u't', u'u', u'v', u'w', u'x', u'y', u'z', u' ', u' ', u' ', u' ', u' ',] 

SCREENCODE_TO_UNICODE[0x41] = u'ù'
SCREENCODE_TO_UNICODE0x42 = unichr(209)
SCREENCODE_TO_UNICODE[0x43] = unichr(201)
SCREENCODE_TO_UNICODE[0x44] = u'ç'
SCREENCODE_TO_UNICODE[0x45] = u'ô'
SCREENCODE_TO_UNICODE[0x46] = unichr(242)
SCREENCODE_TO_UNICODE[0x47] = unichr(236)
SCREENCODE_TO_UNICODE[0x48] = u"£"
SCREENCODE_TO_UNICODE[0x49] = u'ï'
SCREENCODE_TO_UNICODE[0x4a] = u'ü'
SCREENCODE_TO_UNICODE[0x4b] = u'ä'
SCREENCODE_TO_UNICODE[0x4c] = u'Ö'
SCREENCODE_TO_UNICODE[0x4d] = unichr(250)
SCREENCODE_TO_UNICODE[0x4e] = unichr(243)
SCREENCODE_TO_UNICODE[0x4f] = u'ö'
SCREENCODE_TO_UNICODE[0x50] = u'Ü'
SCREENCODE_TO_UNICODE[0x51] = unichr(229)
SCREENCODE_TO_UNICODE[0x52] = u'û'
SCREENCODE_TO_UNICODE[0x53] = u'î'
SCREENCODE_TO_UNICODE[0x54] = u'é'
SCREENCODE_TO_UNICODE[0x55] = u'è'
SCREENCODE_TO_UNICODE[0x55] = u'è'
SCREENCODE_TO_UNICODE[0x56] = unichr(0xf1)
SCREENCODE_TO_UNICODE[0x57] = u'ê'
SCREENCODE_TO_UNICODE[0x58] = unichr(257)
SCREENCODE_TO_UNICODE[0x59] = u'à'
SCREENCODE_TO_UNICODE[0x5a] = unichr(256)

sys.stdout.write("SCREENCODE_TO_UNICODE = [\n    ")
for index in range(len(SCREENCODE_TO_UNICODE)):
    value = SCREENCODE_TO_UNICODE[index]
    sys.stdout.write("%3d, "%(ord(value)))
    if index == len(SCREENCODE_TO_UNICODE) - 1:
        sys.stdout.write("]\n\n")
    elif index % 16 == 15:
        sys.stdout.write("\n    ")

sys.stdout.write("UNICODE_TO_SCREENCODE = {\n    ")
for index in range(len(SCREENCODE_TO_UNICODE)):
    key = SCREENCODE_TO_UNICODE[index]
    sys.stdout.write("%5d:%3d, "%(ord(key), index))
    if index == len(SCREENCODE_TO_UNICODE) - 1:
        sys.stdout.write("}\n\n")
    elif index % 8 == 7:
        sys.stdout.write("\n    ")






#~ sys.stdout.write("UNICODE_TO_SCREENCODE = {\n    ")
#~ for index in range(len(ACE.SCREENCODE_TO_UNICODE)):
    #~ value =  ord(ACE.screencodeToUnicode(chr(index)))
    #~ sys.stdout.write("%d:%d"%(index, value))


