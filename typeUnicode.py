#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter as gui
import tkFont as gui_font

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

win = gui.Tk()

ibox = gui.Entry(win)
ibox.grid(column=0, row=0)

glyphe = gui.StringVar()
#~ font = gui_font.Font(family="DejaVu Sans Mono", size=32)
font = gui_font.Font(family="Atari Classic Int", size=32)
obox = gui.Label(win, textvariable=glyphe, bg="white", font=font)
obox.grid(column=0, row=2)

bt = gui.Button(win, text="SHOW UNICODE", command=lambda ibox=ibox, glyphe=glyphe:writeUnicode(ibox, glyphe))
bt.grid(column=0, row=1)

win.mainloop()