#!/usr/bin/python
# -*- coding: utf-8 -*-

NB_COLS = 40 #TODO: redondant at the moment

ATARI_BLUE = "#4992B9"
ATARI_WHITE = "#e0e0e0"
ATARI_FONTNAME = "Atari Classic Int"
ATARI_DISK = None
ATARI_DISK_FILETYPES=[("Atari 800 image file", "*"),("All files", "*.*"),]
LAST_ATARI_DISK_FNAME = "./ressource/TITREUSE"
ATARI_DIR_NB_COLS = 12
ATARI_FILENAME = "NONAME"

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

class TEMP_TEXT(gui.Toplevel):
    def __init__(self, container, *args, **kwds):
        gui.Toplevel.__init__(self, container)
        self.editor = gui.Text(self, **kwds)
        self.editor.grid()
        if len(args):
            self.setRawText(args[0])
        if len(args) > 1:
            self.title(args[1])
        self.bind("<FocusOut>", self.close)

    def setRawText(self, text):
        self.editor.delete('1.0', 'end')
        self.editor.insert("end", text)
        
    def close(self, event=None):
        self.destroy()

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

def cmdAtariMountDisk(window):
    global LAST_ATARI_DISK_FNAME, ATARI_DISK
    filetypes=[("Atari 800 image file", "*.*"),]
    title="select an Atari disk image file to open"
    initialfile = LAST_ATARI_DISK_FNAME
    sys.stdout.write("-%s-\n"%initialfile)   
    initialdir = os.path.dirname(LAST_ATARI_DISK_FNAME)
    fname = gui_fd.askopenfilename(title=title, parent=window, filetypes=ATARI_DISK_FILETYPES, initialfile=initialdir, initialdir=initialdir)
    if not fname in ("", None):
        if type(fname) != tuple:
            LAST_ATARI_DISK_FNAME = fname
            ATARI_DISK = window.hooks['mountAtariDisk'](fname)

def cmdAtariFileList(window):
    if ATARI_DISK != None:
        fnames = window.hooks['getAtariDiskDirectory'](ATARI_DISK)
        ata_font = gui_font.Font(family=ATARI_FONTNAME, size=16)
        TEMP_TEXT(window, "\n".join(fnames), os.path.basename(LAST_ATARI_DISK_FNAME), bg=ATARI_BLUE, fg=ATARI_WHITE, font=ata_font, width=ATARI_DIR_NB_COLS)

def cmdLoadAtariFile(window):
    global ATARI_FILENAME
    if ATARI_DISK != None:
        fname = gui_sd.askstring(os.path.basename(LAST_ATARI_DISK_FNAME), "Enter credits text name", initialvalue=ATARI_FILENAME)
        if fname in window.hooks['getAtariDiskDirectory'](ATARI_DISK):
            ATARI_FILENAME = fname
            text = window.hooks['screenToUnicode'](ATARI_DISK.readFile(fname))
            setAtariText(window.ata_window.ata_editor, text)

def cmdLoad(window):
    global LAST_FILE_FNAME
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
    menuata.add_command(label="Mount disk", command=lambda window=window:cmdAtariMountDisk(window))
    menuata.add_command(label="Directory", command=lambda window=window:cmdAtariFileList(window))
    menuata.add_command(label="Load file", command=lambda window=window:cmdLoadAtariFile(window))
    menuata.add_command(label="Save file")
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