#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

def getPythonInfoText():
    words = sys.version.split()
    #~ return ("python %s\n%s bits"%(words[0], words[8]))
    return ("python info : %s\n"%str(words))

if sys.version_info[0] < 3:
    # python 2 or less
    import Tkinter as gui
    import tkMessageBox as gui_mb
    import tkSimpleDialog as gui_sd
    import tkFileDialog as gui_fd
    import tkFont as gui_font
else:
    # python 3 or more
    import tkinter as gui
    #~ import tkMessageBox as gui_mb
    #~ import tkSimpleDialog as gui_sd
    #~ import tkFileDialog as gui_fd
    #~ import tkFont as gui_font

    gui_mb = gui
    gui_sd = gui
    gui_fd = gui
    gui_font = gui

if __name__ == "__main__":

