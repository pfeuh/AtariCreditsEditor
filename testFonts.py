#!/usr/bin/python
# -*- coding: utf-8 -*-

import wordProcessor
import atadisk as atadisk
import sys
from dump import *
import Tkinter as tk
import tkFont as tkFont

def nextFont(window, editor):
    window.font_num += 1
    font_name = tkFont.families()[window.font_num]
    sys.stdout.write(font_name + '\n')
    window.title(font_name)
    font = tkFont.Font(family=font_name, size=20, weight='bold')
    editor = tk.Text(window, font=font)
    editor.grid(column=0,row=0)
    for x in range(0, len(text), NB_COLS):
        editor.insert("end", text[x: x + NB_COLS])
        editor.insert("end", "\n")
    window.bt['command'] = lambda window=window,editor=editor:nextFont(window, editor)

if __name__ == "__main__":

    with open("./text/msieurReflex.utf", "r") as fp:
        text = fp.read(-1).decode("utf-8")
    
        
    #~ sys.stdout.write(dump(text, 40))

    #~ text = asciiToScreen(text)    
    #~ with open("./ressource/aide2.text", "wb") as fp:
        #~ fp.write(text)

    window = tk.Tk()
    window.bt = tk.Button(window, text="Next font")
    window.bt.grid(column=1, row=0)
    window.bt['command'] = lambda window=window,editor=None:nextFont(window, editor)
    window.font_num = -1
    with open ("ressource/families.txt", "w") as fp:
        for font_name in tkFont.families():
            fp.write(font_name)
            fp.write("\n")
            if "atari" in font_name.lower():
                print font_name
    #~ window.mainloop()
    
    # DejaVu Sans Mono
    # Tlwg Typist
    # Noto Sans Mono CJK SC

    
    