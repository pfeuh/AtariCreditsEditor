#!/usr/bin/python
# -*- coding: utf-8 -*-

import atadisk as atadisk
import sys
from dump import *

EMPTY = ""
CHAR_SPACE = " "

SCREEN_TO_ASCII = [
    ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', 
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?',
    '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', 
    ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
    ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
    ' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', ' ', ' ', ' ', ' ', 
    ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
    ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
    ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
    ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
    ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
    ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
    ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
    ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ]

def listToDico(table, dico_name):
    ret_dico = {}
    sys.stdout.write("%s =\n{\n    "%(dico_name))
    for index in range(len(table)):
        key = table[index]
        if key == "'":
            if not key in ret_dico.keys():
                sys.stdout.write('"%s":%3d, '%(key, index))
        elif key == "\\":
            if not key in ret_dico.keys():
                sys.stdout.write("'\\\\':%3d, "%(index))
        else:
            if not key in ret_dico.keys():
                sys.stdout.write("'%s':%3d, "%(key, index))           
        if index % 4 == 3:
            sys.stdout.write("\n    ")
        ret_dico[key] = index
    sys.stdout.write("\n}\n")

listToDico(SCREEN_TO_ASCII, "ASCII_TO_SCREEN")
sys.exit()

if __name__ == "__main__":

    disk = atadisk.VIRTUAL_DISK("./ressource/TITREUSE")
    #~ sys.stdout.write(disk.directory())
    font = disk.readFile("ACCENTUE.FNT")

    import Tkinter as TK
    win = TK.Tk()
    win.mainloop()
    
    