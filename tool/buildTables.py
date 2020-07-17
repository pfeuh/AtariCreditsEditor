#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

target_fname = "atariScreenEncodeDecode.py"

d01 = 16
d02 = 17
d03 = 18
d04 = 19
d05 = 20
d06 = 21
d07 = 22
d08 = 23
dummies = (d01, d02, d03, d04, d05, d06, d07, d08)
dummy_char = ord('?')

PART_1 = """#!/usr/bin/python
# -*- coding: utf-8 -*-

#--------------------------------
# VERSION 1.00
# DON'T EDIT THIS GENERATED FILE,
# USE RATHER buildTables.py
#--------------------------------

import sys

EMPTY = unicode("")

"""

PART_2 = """def screencodeToUnicode(text,encode=None):
    ret_text  = EMPTY
    for car in text:
        car = unichr(SCREENCODE_TO_UNICODE[ord(car)])
        ret_text += car
    return ret_text

def unicodeToScreencode(text,encode=None):
    ret_text  = EMPTY
    for car in text:
        ucode = ord(car)
        car = chr(UNICODE_TO_SCREENCODE[ucode])
        ret_text += car
    return ret_text

"""

def printScreencodeToUnicode(table):
    tmax = len(table)
    text = "SCREENCODE_TO_UNICODE = [\n    "
    for index in range(tmax):
        text += "0x%04x, "%ord(table[index])
        if (index + 1) == tmax:
            text += "]\n\n"
        elif (index % 16) == 15:
            text += "\n    "
    return text

def printUnicodeToScreencode(table):
    tmax = len(table)
    text = "UNICODE_TO_SCREENCODE = {\n    "
    keys = table.keys()
    keys.sort()
    for index, key in enumerate(keys):
        text += "0x%04x:0x%02x, "%(key, table[key])
        if (index + 1) == tmax:
            text += "}\n\n"
        elif (index % 8) == 7:
            text += "\n    "
    return text

def generateFile(fp):
    fp.write(PART_1)
    fp.write(printScreencodeToUnicode(SCREENCODE_TO_UNICODE))
    fp.write(printUnicodeToScreencode(UNICODE_TO_SCREENCODE))
    fp.write(PART_2)
    fp.close()

SCREENCODE_TO_UNICODE = [
    u' ', u'!', u'"', u'#', u'$', u'%', u'&', u"'", u'(', u')', u'*', u'+', u',', u'-', u'.', u'/', 
    u'0', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9', u':', u';', u'<', u'=', u'>', u'?',
    u'@', u'A', u'B', u'C', u'D', u'E', u'F', u'G', u'H', u'I', u'J', u'K', u'L', u'M', u'N', u'O', 
    u'P', u'Q', u'R', u'S', u'T', u'U', u'V', u'W', u'X', u'Y', u'Z', u'[', u'\\',u']', u'^', u'_', 
    u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', 
    u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', 
    u' ', u'a', u'b', u'c', u'd', u'e', u'f', u'g', u'h', u'i', u'j', u'k', u'l', u'm', u'n', u'o', 
    u'p', u'q', u'r', u's', u't', u'u', u'v', u'w', u'x', u'y', u'z', u' ', u' ', u' ', u' ', u' ',] 

SCREENCODE_TO_UNICODE[0x40] = unichr(225) # a minuscule accent aigu
SCREENCODE_TO_UNICODE[0x41] = unichr(249) # u minuscule accent grave
SCREENCODE_TO_UNICODE[0x42] = unichr(209) # n majuscule tild
SCREENCODE_TO_UNICODE[0x43] = unichr(201) # e majuscule accent aigu
SCREENCODE_TO_UNICODE[0x44] = unichr(231) # c minuscule cedille
SCREENCODE_TO_UNICODE[0x45] = unichr(244) # o minuscule accent circonflexe
SCREENCODE_TO_UNICODE[0x46] = unichr(242) # o minuscule accent grave
SCREENCODE_TO_UNICODE[0x47] = unichr(236) # i minuscule accent grave
SCREENCODE_TO_UNICODE[0x48] = unichr(163) # livre (pound)
SCREENCODE_TO_UNICODE[0x49] = unichr(239) # i minuscule trema
SCREENCODE_TO_UNICODE[0x4a] = unichr(252) # u minuscule trema
SCREENCODE_TO_UNICODE[0x4b] = unichr(228) # a minuscule trema
SCREENCODE_TO_UNICODE[0x4c] = unichr(214) # o majuscule trema
SCREENCODE_TO_UNICODE[0x4d] = unichr(250) # u minuscule accent aigu
SCREENCODE_TO_UNICODE[0x4e] = unichr(243) # o minuscule accent aigu
SCREENCODE_TO_UNICODE[0x4f] = unichr(246) # o minuscule trema
SCREENCODE_TO_UNICODE[0x50] = unichr(220) # U majuscule trema
SCREENCODE_TO_UNICODE[0x51] = unichr(226) # a minuscule accent circonflexe 
SCREENCODE_TO_UNICODE[0x52] = unichr(251) # u minuscule accent circonflexe
SCREENCODE_TO_UNICODE[0x53] = unichr(238) # i minuscule accent circonflexe
SCREENCODE_TO_UNICODE[0x54] = unichr(233) # e minuscule accent aigu
SCREENCODE_TO_UNICODE[0x55] = unichr(232) # e minuscule accent grave
SCREENCODE_TO_UNICODE[0x55] = unichr(232) # e minuscule accent grave
SCREENCODE_TO_UNICODE[0x56] = unichr(241) # n minuscule tild
SCREENCODE_TO_UNICODE[0x57] = unichr(234) # e minuscule accent circonflexe
SCREENCODE_TO_UNICODE[0x58] = unichr(229) # a minuscule cercle
SCREENCODE_TO_UNICODE[0x59] = unichr(224) # a minuscule accent grave
SCREENCODE_TO_UNICODE[0x5a] = unichr(197) # reverted exclamation mark
SCREENCODE_TO_UNICODE[0x5b] = unichr(d01) # escape
SCREENCODE_TO_UNICODE[0x5c] = unichr(d02) # up arrow
SCREENCODE_TO_UNICODE[0x5d] = unichr(d03) # down arrow
SCREENCODE_TO_UNICODE[0x5e] = unichr(d04) # left arrow
SCREENCODE_TO_UNICODE[0x5f] = unichr(d05) # up arrow
SCREENCODE_TO_UNICODE[0x60] = unichr(161) # i majuscule avec un point au dessus
SCREENCODE_TO_UNICODE[0x7b] = unichr(196) # a majuscule trema
SCREENCODE_TO_UNICODE[0x7c] = unichr(124) # pipe
SCREENCODE_TO_UNICODE[0x7d] = unichr(d06) # espece de RETURN
SCREENCODE_TO_UNICODE[0x7e] = unichr(d07) # triangle plein vers droite
SCREENCODE_TO_UNICODE[0x7f] = unichr(d08) # triangle plein vers gauche

UNICODE_TO_SCREENCODE = {}
test_cars = []
for car_num in range(len(SCREENCODE_TO_UNICODE)):
    ucod = ord(SCREENCODE_TO_UNICODE[car_num])
    if ucod in dummies:
        car_num = dummy_char
    else:
        if car_num in test_cars:
            raise Exception("car %s for unicode 0x%4x already used!\n"%car_num, ucode)
        else:
            test_cars.append(car_num)
    UNICODE_TO_SCREENCODE[ucod]= car_num

generateFile(open("./" + target_fname, "w"))
generateFile(open("./../" + target_fname, "w"))
generateFile(sys.stdout)
sys.exit()

if __name__ == "__main__":
    
    import Tkinter as gui
    import tkFont as gui_font

    ATARI_BLUE = "#4992B9"
    ATARI_WHITE = "#e0e0e0"

    def myquit(event):
        win.quit()

    def writeUnicode(ibox, glyphe):
        value = None
        text = ibox.get().strip()
        if text.startswith("$"):
            value = int(text[1:], 16)
        elif text.lower().startswith("0x"):
            value = int(text[2:], 16)
        elif text.lower().startswith("0b"):
            value = int(text[2:], 2)
        else:
            value = int(text)
        glyphe.set(" " + unichr(value) + " ")

    def returnHook(event):
        writeUnicode(ibox, glyphe)

    win = gui.Tk()
    img = gui.PhotoImage(file="./ressource/accentued_font.png")
    #~ img = img.resize(image.width() * 2, image.height() * 2)
    img = img.zoom(2, 2)
    #~ font = gui_font.Font(family="DejaVu Sans Mono", size=40)
    font = gui_font.Font(family="Atari Classic Int", size=32)

    ata_text = gui.Label(win, image = img)
    ata_text.grid(column=0, row=0)

    scr_text = gui.Text(win, width=16, height=8, font=font, bg=ATARI_BLUE, fg=ATARI_WHITE)
    scr_text.grid(column=1, row=0)
    scr_text.insert("end", "".join(SCREENCODE_TO_UNICODE))

    font = gui_font.Font(family="DejaVu Sans Mono", size=24)
    scr_text2 = gui.Text(win, width=16, height=8, font=font)
    scr_text2.grid(column=1, row=1)
    scr_text2.insert("end", "".join(SCREENCODE_TO_UNICODE))

    #~ wrk_zone = gui.Frame(win)
    #~ wrk_zone.grid(column=0, row=1)
    #~ ibox = gui.Entry(wrk_zone)
    #~ ibox.grid(column=0, row=0)
    #~ glyphe = gui.StringVar()
    #~ obox = gui.Label(wrk_zone, textvariable=glyphe, bg="white")
    #~ obox.grid(column=0, row=2)
    #~ bt = gui.Button(wrk_zone, text="SHOW UNICODE", command=lambda ibox=ibox, glyphe=glyphe:writeUnicode(ibox, glyphe))
    #~ bt.grid(column=0, row=1)
    #~ ibox.bind("<Return>", returnHook)
    
    font = gui_font.Font(family="Atari Classic Int", size=32)
    #~ font = gui_font.Font(family="Atari Classic Chunky", size=32)
    scr_text3 = gui.Text(win, width=22, height=8, font=font, bg=ATARI_BLUE, fg=ATARI_WHITE)
    scr_text3.grid(column=0, row=1)
    text = unicode()
    for index in range(0, 65536, 16):
        text += "%4x "%index
        for x in range(16):
            text += unichr(index + x)
        text += "\n"
    scr_text3.insert("end", text)
    
    win.bind("<Escape>", myquit)

    win.mainloop()