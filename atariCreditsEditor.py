#!/usr/bin/python
# -*- coding: utf-8 -*-

import wordProcessor
import atadisk as atadisk
import sys
from dump import *
import Tkinter as tk
import tkFont as tkFont

NB_COLS = 40
EMPTY = unicode("")
CHAR_SPACE = " "

SCREEN_TO_ASCII = [
    u' ', u'!', u'"', u'#', u'$', u'%', u'&', u"'", u'(', u')', u'*', u'+', u',', u'-', u'.', u'/', 
    u'0', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9', u':', u';', u'<', u'=', u'>', u'?',
    u'@', u'A', u'B', u'C', u'D', u'E', u'F', u'G', u'H', u'I', u'J', u'K', u'L', u'M', u'N', u'O', 
    u'P', u'Q', u'R', u'S', u'T', u'U', u'V', u'W', u'X', u'Y', u'Z', u'[', u'\\',u']', u'^', u'_', 
    u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', 
    u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', 
    u' ', u'a', u'b', u'c', u'd', u'e', u'f', u'g', u'h', u'i', u'j', u'k', u'l', u'm', u'n', u'o', 
    u'p', u'q', u'r', u's', u't', u'u', u'v', u'w', u'x', u'y', u'z', u' ', u' ', u' ', u' ', u' ', 
    u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', 
    u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', 
    u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', 
    u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', 
    u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', 
    u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', 
    u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', 
    u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', ]

ASCII_TO_SCREEN = {
    ' ':  0, '!':  1, '"':  2, '#':  3, 
    '$':  4, '%':  5, '&':  6, "'":  7, 
    '(':  8, ')':  9, '*': 10, '+': 11, 
    ',': 12, '-': 13, '.': 14, '/': 15, 
    '0': 16, '1': 17, '2': 18, '3': 19, 
    '4': 20, '5': 21, '6': 22, '7': 23, 
    '8': 24, '9': 25, ':': 26, ';': 27, 
    '<': 28, '=': 29, '>': 30, '?': 31, 
    '@': 32, 'A': 33, 'B': 34, 'C': 35, 
    'D': 36, 'E': 37, 'F': 38, 'G': 39, 
    'H': 40, 'I': 41, 'J': 42, 'K': 43, 
    'L': 44, 'M': 45, 'N': 46, 'O': 47, 
    'P': 48, 'Q': 49, 'R': 50, 'S': 51, 
    'T': 52, 'U': 53, 'V': 54, 'W': 55, 
    'X': 56, 'Y': 57, 'Z': 58, '[': 59, 
    '\\': 60, ']': 61, '^': 62, '_': 63, 
    'a': 97, 'b': 98, 'c': 99, 
    'd':100, 'e':101, 'f':102, 'g':103, 
    'h':104, 'i':105, 'j':106, 'k':107, 
    'l':108, 'm':109, 'n':110, 'o':111, 
    'p':112, 'q':113, 'r':114, 's':115, 
    't':116, 'u':117, 'v':118, 'w':119, 
    'x':120, 'y':121, 'z':122, }

def screenToAscii(text,encode=None):
    ret_text  = EMPTY
    for car_num, car in enumerate(text):
        index = ord(car)
        assert index < 256
        if index < 128:
            car = SCREEN_TO_ASCII[index]
            if index and (car == CHAR_SPACE):
                # not implemented or accentued
                if index == 0x41:
                    car = u'ù'
                elif index == 0x42:
                    car = unichr(209)
                elif index == 0x43:
                    car = unichr(201)
                elif index == 0x44:
                    car = u'ç'
                elif index == 0x45:
                    car = u'ô'
                elif index == 0x46:
                    car = unichr(242)
                elif index == 0x47:
                    car = unichr(236)
                elif index == 0x48:
                    car = u"£"
                elif index == 0x49:
                    car = u'ï'
                elif index == 0x4a:
                    car = u'ü'
                elif index == 0x4b:
                    car = u'ä'
                elif index == 0x4c:
                    car = u'Ö'
                elif index == 0x4d:
                    car = unichr(250)
                elif index == 0x4e:
                    car = unichr(243)
                elif index == 0x4f:
                    car = u'ö'
                elif index == 0x50:
                    car = u'Ü'
                elif index == 0x51:
                    car = unichr(229)
                elif index == 0x52:
                    car = u'û'
                elif index == 0x53:
                    car = u'î'
                elif index == 0x54:
                    car = u'é'
                elif index == 0x55:
                    car = u'è'
                elif index == 0x55:
                    car = u'è'
                elif index == 0x56:
                    car = unichr(0xf1)
                elif index == 0x57:
                    car = u'ê'
                elif index == 0x58:
                    car = unichr(257)
                elif index == 0x59:
                    car = u'à'
                elif index == 0x5a:
                    car = unichr(256)
                else:
                    car = u'?'
                    sys.stdout.write("%02x\n"%index)
        else:
            # non ascii character
            pass
        ret_text += car
    return ret_text
            
def asciiToScreen(text):
    ret_text  = EMPTY
    for car in text:
        index = ASCII_TO_SCREEN[car]
        ret_text += chr(index)
    return ret_text

def readPcText(fname):
    with open(fname, "r") as fp:
        text = fp.read(-1).decode("utf-8")
    formated_text = wordProcessor.TEXT_BUFFER(text, cols=NB_COLS).getFormatedText()
    return formated_text

def loadAtariText(fname, disk):
    print fname
    text = disk.readFile(fname)
    formated_text = screenToAscii(text)
    return formated_text
    
if __name__ == "__main__":

    disk = atadisk.VIRTUAL_DISK("./ressource/CREDITS")
    #~ sys.stdout.write(disk.directory())

    #~ text = readPcText("./text/msieurReflex.utf")
    text = readPcText("./text/utest.utf")
    #~ text = loadAtariText("AIDE.ECR", disk)

    window = tk.Tk()
    #~ font_name = "DejaVu Sans Mono"
    font_name = "Atari Classic Int"    
    window.title(font_name)
    font = tkFont.Font(family=font_name, size=16)#, weight='bold')
    editor = tk.Text(window, font=font, width=NB_COLS + 4, padx=0, pady=0, wrap=tk.NONE, bg="#4992B9", fg="#e0e0e0")
    editor.grid(column=0,row=0)
    raw_font = tkFont.Font(size=12)
    raw_editor = tk.Text(window, width=NB_COLS, font=raw_font)
    raw_editor.grid(column=1,row=0)
    #~ editor.insert("end", text)
    for x in range(0, len(text), NB_COLS):
        editor.insert("end", "  " + text[x: x + NB_COLS])
        editor.insert("end", "\n")
    window.mainloop()

    # DejaVu Sans Mono
    # Tlwg Typist
    # Noto Sans Mono CJK SC

    
    