#!/usr/bin/python
# -*- coding: utf-8 -*-

NB_COLS = 40 #TODO: redondant at the moment

ATARI_BLUE = "#4992B9"
ATARI_WHITE = "#e0e0e0"
ATARI_FONTNAME = "Atari Classic Int"

RAW_FONTNAME = "DejaVu Sans Mono"
RAW_FILETYPES = [("All files", "*.*"), ("ascii credits", "*.txt"), ("extended credits", "*.utf")]

LAST_FILE_FNAME = "./text/noname.utf"

import sys
import os

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

def setAtariText(editor, text):
    editor.delete('1.0', 'end')
    for x in range(0, len(text), NB_COLS):
        editor.insert("end", "  " + text[x: x + NB_COLS])
        editor.insert("end", "\n")

def setRawText(editor, text):
    editor.delete('1.0', 'end')
    editor.insert("end", text)

def getAtariEditor(window):
    ata_font = gui_font.Font(family=ATARI_FONTNAME, size=16)
    ata_editor = gui.Text(window, font=ata_font, width=NB_COLS + 4, wrap=gui.NONE, bg=ATARI_BLUE, fg=ATARI_WHITE)
    ata_editor.grid(column=0,row=0)
    return ata_editor

def getRawEditor(window):
    raw_font = gui_font.Font(family=RAW_FONTNAME, size=12)
    raw_editor = gui.Text(window, font=raw_font, width=NB_COLS)
    raw_editor.grid(column=1,row=0)
    return raw_editor

def cmdLoad(window):
    global LAST_FILE_FNAME
    filetypes=[("All files", "*.*"), ("ascii credits", "*.txt"), ("extended credits", "*.utf")]
    title="select a file to open"
    initialfile = LAST_FILE_FNAME
    sys.stdout.write("-%s-\n"%initialfile)   
    initialdir = os.path.dirname(LAST_FILE_FNAME)
    fname = gui_fd.askopenfilename(title=title, parent=window, filetypes=RAW_FILETYPES, initialfile=initialdir, initialdir=initialdir)
    sys.stdout.write("<%s>\n"%str(fname))
    print type(fname)
    if not fname in ("", None):
        if type(fname) != tuple:
            LAST_FILE_FNAME = fname
            text = window.hooks['readPcText'](fname)
            setRawText(window.raw_editor, text)
            window.title(os.path.basename(fname))

def cmdRefreshText(window):
    text = window.raw_editor.get('1.0', 'end')
    formated_text = window.hooks['formatAtariText'](text)
    setAtariText(window.ata_window.ata_editor, formated_text)

def getMenu(window):
    menu = gui.Menu(window, fg="white", bg="black")

    # MENU FILES
    menufile = gui.Menu(tearoff=0)
    menufile.add_command(label="New")
    menufile.add_command(label="Load", command=lambda window=window:cmdLoad(window))
    menufile.add_command(label="Save")
    menufile.add_separator()
    menufile.add_command(label="Quit")
    menu.add_cascade(label="Files", menu=menufile)

    menupref = gui.Menu(tearoff=0)
    menupref.add_command(label="Accentuated")
    menupref.add_command(label="Graphic")
    menu.add_cascade(label="Preferences", menu=menupref)

    menuata = gui.Menu(tearoff=0)
    menuata.add_command(label="Refresh text", command=lambda window=window:cmdRefreshText(window))
    menuata.add_separator()
    menuata.add_command(label="Mount disk")
    menuata.add_command(label="Directory")
    menuata.add_command(label="Save file")
    menuata.add_command(label="Show file")
    menu.add_cascade(label="Atari 800", menu=menuata)

    return menu
    
def getWindow(hooks):
    window = gui.Tk()
    window.hooks = hooks
    window.config(menu=getMenu(window))
    window.raw_editor = getRawEditor(window)
    window.ata_window = gui.Toplevel(window)
    window.ata_window.title(os.path.splitext(os.path.basename(sys.argv[0]))[0])
    window.ata_window.ata_editor = getAtariEditor(window.ata_window)
    return window

if __name__ == "__main__":

    pass