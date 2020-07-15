#!/usr/bin/python
# -*- coding: utf-8 -*-

import wordProcessor
import atadisk
import sys
import gui

NB_COLS = 40
EMPTY = unicode("")
CHAR_SPACE = " "

# TODO: Bug, CTRL-B should give ~N with ATARI files. Works fine with PC files.
# TODO: Inhibit atari window closing.
# TODO: implement file modified flag for raw text
# TODO: implement undo/redo for raw text
# TODO: implement alert boxes for errors
# TODO: make the atari screen read-only

SCREENCODE_TO_UNICODE = [
     32,  33,  34,  35,  36,  37,  38,  39,  40,  41,  42,  43,  44,  45,  46,  47, 
     48,  49,  50,  51,  52,  53,  54,  55,  56,  57,  58,  59,  60,  61,  62,  63, 
     64,  65,  66,  67,  68,  69,  70,  71,  72,  73,  74,  75,  76,  77,  78,  79, 
     80,  81,  82,  83,  84,  85,  86,  87,  88,  89,  90,  91,  92,  93,  94,  95, 
     32, 249,  32, 201, 231, 244, 242, 236, 163, 239, 252, 228, 214, 250, 243, 246, 
    220, 229, 251, 238, 233, 232, 241, 234, 257, 224, 256,  32,  32,  32,  32,  32, 
     32,  97,  98,  99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 
    112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122,  32,  32,  32,  32,  32, ]

def screencodeToUnicode(text,encode=None):
    ret_text  = EMPTY
    for car in text:
        car = unichr(SCREENCODE_TO_UNICODE[ord(car)])
        ret_text += car
    return ret_text

UNICODE_TO_SCREENCODE = {
       32:  0,    33:  1,    34:  2,    35:  3,    36:  4,    37:  5,    38:  6,    39:  7, 
       40:  8,    41:  9,    42: 10,    43: 11,    44: 12,    45: 13,    46: 14,    47: 15, 
       48: 16,    49: 17,    50: 18,    51: 19,    52: 20,    53: 21,    54: 22,    55: 23, 
       56: 24,    57: 25,    58: 26,    59: 27,    60: 28,    61: 29,    62: 30,    63: 31, 
       64: 32,    65: 33,    66: 34,    67: 35,    68: 36,    69: 37,    70: 38,    71: 39, 
       72: 40,    73: 41,    74: 42,    75: 43,    76: 44,    77: 45,    78: 46,    79: 47, 
       80: 48,    81: 49,    82: 50,    83: 51,    84: 52,    85: 53,    86: 54,    87: 55, 
       88: 56,    89: 57,    90: 58,    91: 59,    92: 60,    93: 61,    94: 62,    95: 63, 
       32: 64,   249: 65,    32: 66,   201: 67,   231: 68,   244: 69,   242: 70,   236: 71, 
      163: 72,   239: 73,   252: 74,   228: 75,   214: 76,   250: 77,   243: 78,   246: 79, 
      220: 80,   229: 81,   251: 82,   238: 83,   233: 84,   232: 85,   241: 86,   234: 87, 
      257: 88,   224: 89,   256: 90,    32: 91,    32: 92,    32: 93,    32: 94,    32: 95, 
       32: 96,    97: 97,    98: 98,    99: 99,   100:100,   101:101,   102:102,   103:103, 
      104:104,   105:105,   106:106,   107:107,   108:108,   109:109,   110:110,   111:111, 
      112:112,   113:113,   114:114,   115:115,   116:116,   117:117,   118:118,   119:119, 
      120:120,   121:121,   122:122,    32:123,    32:124,    32:125,    32:126,    32:127, }

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

def unicodeToScreencode(text,encode=None):
    ret_text  = EMPTY
    for car in text:
        car = chr(UNICODE_TO_SCREENCODE[ord(car)])
        ret_text += car
    return ret_text

def readPcText(fname):
    with open(fname, "r") as fp:
        text = fp.read(-1).decode("utf-8")
    return text

def formatAtariText(text):
    formated_text = wordProcessor.TEXT_BUFFER(text, cols=NB_COLS).getFormatedText()
    return formated_text

def mountAtariDisk(fname):
    disk = atadisk.VIRTUAL_DISK(fname)
    return disk

def createAtariDisk(fname):
    disk = atadisk.createDisk(fname)
    return disk

def getAtariDiskDirectory(disk):
    return disk.getDirectory()

def getAtariDiskVerboseDirectory(disk):
    print disk.directory()
    return disk.directory()

if __name__ == "__main__":

    hooks = {
        'readPcText':readPcText,
        'mountAtariDisk':mountAtariDisk,
        'getAtariDiskDirectory':getAtariDiskDirectory,
        'getAtariDiskVerboseDirectory':getAtariDiskVerboseDirectory,
        'screencodeToUnicode':screencodeToUnicode,
        'unicodeToScreencode':unicodeToScreencode,
        'createAtariDisk':createAtariDisk,
        'formatAtariText':formatAtariText}

    window = gui.getWindow(hooks)
    window.mainloop()
