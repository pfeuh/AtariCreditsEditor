#!/usr/bin/python
# -*- coding: utf-8 -*-

import wordProcessor
from atariScreenEncodeDecode import *
import atadisk
import sys
import gui

NB_COLS = 40
CHAR_SPACE = " "

# TODO: Bug, CTRL-B should give ~N with ATARI files. Works fine with PC files.
# TODO: Inhibit atari window closing.
# TODO: implement file modified flag for raw text
# TODO: implement undo/redo for raw text
# TODO: implement alert boxes for errors
# TODO: make the atari screen read-only

def readPcText(fname):
    #return an unicode string from an utf-8 PC file
    with open(fname, "r") as fp:
        text = fp.read(-1).decode("utf-8")
    return text

def formatAtariText(text):
    # format a text with justification right, left, centered and both sides
    formated_text = wordProcessor.TEXT_BUFFER(text, cols=NB_COLS).getFormatedText()
    return formated_text

def mountAtariDisk(fname):
    # mount an atari disk image
    disk = atadisk.VIRTUAL_DISK(fname)
    return disk

def createAtariDisk(fname):
    # create a new atari disk image
    disk = atadisk.createDisk(fname)
    return disk

def getAtariDiskDirectory(disk):
    # get atari disk image file list
    return disk.getDirectory()

def getAtariDiskVerboseDirectory(disk):
    return disk.directory()

def formatAtariText(text):
    # get atari disk image file list and some extra info as a text
    formated_text = wordProcessor.TEXT_BUFFER(text, cols=NB_COLS).getFormatedText()
    return formated_text

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
