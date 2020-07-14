#!/usr/bin/python
# -*- coding: utf-8 -*-

import atadisk as atadisk
import sys
from dump import *
import Tkinter as tk

EMPTY = u""
CHAR_SPACE = " "

if __name__ == "__main__":

    with open("./text/msieurReflex.utf", "r") as fp:
        text = fp.read(-1).decode("utf-8")
    print type(text)
    
    window = tk.Tk()
    editor = tk.Text(window)
    editor.grid()
    editor.insert("end", text)
    window.mainloop()
    
    #~ print text
        