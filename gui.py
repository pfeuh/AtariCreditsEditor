#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import dump
import shutil
from wordProcessor import getNbCols
NB_COLS = getNbCols()

#~ NB_COLS = 40 #TODO: redondant at the moment

ATARI_BLUE = "#4992B9"
ATARI_WHITE = "#e0e0e0"
ATARI_FONTNAME = "Atari Classic Int"
ATARI_DISK = None
ATARI_DISK_FILETYPES=[("Atari 800 image file", "*"),("All files", "*.*"),]
CURRENT_ATARI_DISK_FNAME = "./ressource/TITREUSE"
ATARI_DIR_NB_COLS = 12
ATARI_DIR_VB_NB_COLS = 18
CURRENT_ATARI_FILENAME = "NONAME"

RAW_FONTNAME = "DejaVu Sans Mono"
RAW_FILETYPES = [("All files", "*.*"), ("ascii credits", "*.txt"), ("extended credits", "*.utf")]
RAW_EXT = ".utf"
DEFAULT_FNAME = "./text/noname.utf"
CURRENT_FILE_FNAME = DEFAULT_FNAME
LEFT_MARGIN = 2
RIGHT_MARGIN = 2

CONFIG = (CURRENT_FILE_FNAME, CURRENT_ATARI_DISK_FNAME)

DEBUG = "-debug" in sys.argv

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

def refreshInfo(window):
    global CURRENT_FILE_FNAME
    window.title(os.path.basename(CURRENT_FILE_FNAME))

def loadPcText(window, fname):
    global CURRENT_FILE_FNAME
    text = window.hooks['readPcText'](fname)
    setRawText(window.raw_editor, text)
    CURRENT_FILE_FNAME = fname
    refreshInfo(window)

def mountAtariDisk(window, fname):
    global CURRENT_ATARI_DISK_FNAME, ATARI_DISK
    ATARI_DISK = window.hooks['mountAtariDisk'](fname)
    CURRENT_ATARI_DISK_FNAME = fname
    if DEBUG:
        sys.stdout.write("disk %s mounted!\n"%fname)

def getConfname():
    return os.path.splitext(sys.argv[0])[0] + ".cfg" 

def saveConf(window):
    with open(getConfname(), "w") as fp:
        for item in CONFIG:
            fp.write(item.encode('utf8'))
            fp.write('\n')

def loadConf(window):
    values = []
    with open(getConfname(), "r") as fp:
        for item in CONFIG:
            values.append(fp.readline().strip().decode('utf8'))
    # CURRENT_FILE_FNAME
    fname = values[0]
    try:
        loadPcText(window, fname)
        if DEBUG:
            sys.stdout.write("text %s loaded!\n"%fname)
    except:
        if DEBUG:
            sys.stdout.write("Can't load %s\n"%fname)
    #CURRENT_ATARI_DISK_FNAME
    fname = values[1]
    try:
        mountAtariDisk(window, fname)
    except:
        if DEBUG:
            sys.stdout.write("Can't mount Atari disk %s!\n"%fname)
    
def setAtariText(editor, text):
    editor.delete('1.0', 'end')
    for x in range(0, len(text), NB_COLS):
        editor.insert("end", " " * LEFT_MARGIN + text[x: x + NB_COLS])
        editor.insert("end", "\n")

def setRawText(editor, text):
    editor.delete('1.0', 'end')
    editor.insert("end", text)

def getAtariEditor(window):
    ata_font = gui_font.Font(family=ATARI_FONTNAME, size=16)
    ata_editor = gui.Text(window, font=ata_font, width=NB_COLS + LEFT_MARGIN + RIGHT_MARGIN, wrap=gui.NONE, bg=ATARI_BLUE, fg=ATARI_WHITE)
    ata_editor.grid(column=0,row=0)
    return ata_editor

def getRawEditor(window):
    raw_font = gui_font.Font(family=RAW_FONTNAME, size=12)
    raw_editor = gui.Text(window, font=raw_font, width=40, wrap="word")
    raw_editor.grid(column=1,row=0)
    return raw_editor

def cmdNew(window):
    global CURRENT_FILE_FNAME
    title="select a file to open"
    setRawText(window.raw_editor, unicode())
    CURRENT_FILE_FNAME = DEFAULT_FNAME
    refreshInfo(window)

def cmdLoad(window):
    global CURRENT_FILE_FNAME
    title="select a file to open"
    initialfile = CURRENT_FILE_FNAME
    initialdir = os.path.dirname(CURRENT_FILE_FNAME)
    fname = gui_fd.askopenfilename(title=title, parent=window, filetypes=RAW_FILETYPES, initialfile=initialdir, initialdir=initialdir)
    if not fname in ("", None):
        if type(fname) != tuple:
            loadPcText(window, fname)

def cmdSave(window, fname=None, keep_name=True):
    global CURRENT_FILE_FNAME
    if fname == None:
        fname = CURRENT_FILE_FNAME
    text = window.raw_editor.get('1.0', 'end')
    with open(fname, "w") as fp:
        fp.write(text.encode('utf8'))
    if not keep_name:
        CURRENT_FILE_FNAME = fname
        window.title(os.path.basename(fname))
     
def cmdSaveAs(window):
    global CURRENT_FILE_FNAME
    dirname = os.path.dirname(CURRENT_FILE_FNAME)
    fname = gui_fd.asksaveasfilename(title="Select a SAVE AS name", initialdir=dirname, initialfile=CURRENT_FILE_FNAME, filetypes=RAW_FILETYPES, defaultextension=RAW_EXT)
    if not fname in ("", None):
        if type(fname) != tuple:
            cmdSave(window, fname, keep_name=False)

def cmdSaveCopyAs(window):
    global CURRENT_FILE_FNAME
    dirname = os.path.dirname(CURRENT_FILE_FNAME)
    fname = gui_fd.asksaveasfilename(title="Select a SAVE AS name", initialdir=dirname, initialfile=CURRENT_FILE_FNAME, filetypes=RAW_FILETYPES, defaultextension=RAW_EXT)
    if not fname in ("", None):
        if type(fname) != tuple:
            cmdSave(window, fname, keep_name=True)

def cmdQuit(window):
    #~ saveConf(window)
    window.quit()
    
def cmdRefreshAtariScreen(window):
    text = window.raw_editor.get('1.0', 'end')
    formated_text = window.hooks['formatAtariText'](text)
    setAtariText(window.ata_window.ata_editor, formated_text)

def cmdAtariMountDisk(window):
    global CURRENT_ATARI_DISK_FNAME, ATARI_DISK
    title="select an Atari disk image to open"
    initialfile = CURRENT_ATARI_DISK_FNAME
    initialdir = os.path.dirname(CURRENT_ATARI_DISK_FNAME)
    fname = gui_fd.askopenfilename(title=title, parent=window, filetypes=ATARI_DISK_FILETYPES, initialfile=initialdir, initialdir=initialdir)
    if not fname in ("", None):
        if type(fname) != tuple:
            mountAtariDisk(window, fname)
            #~ CURRENT_ATARI_DISK_FNAME = fname
            #~ ATARI_DISK = window.hooks['mountAtariDisk'](fname)

def cmdAtariCreateDisk(window):
    global CURRENT_ATARI_DISK_FNAME, ATARI_DISK
    title="select an Atari disk image to create"
    initialdir = os.path.dirname(CURRENT_ATARI_DISK_FNAME)
    fname = gui_fd.askopenfilename(title=title, parent=window, filetypes=ATARI_DISK_FILETYPES, initialfile=initialdir, initialdir=initialdir)
    fname = gui_fd.asksaveasfilename(title="title", initialdir=initialdir, initialfile=CURRENT_FILE_FNAME, filetypes=ATARI_DISK_FILETYPES)
    if not fname in ("", None):
        if type(fname) != tuple:
            CURRENT_ATARI_DISK_FNAME = fname
            ATARI_DISK = window.hooks['createAtariDisk'](fname)

def cmdAtariFileList(window):
    if ATARI_DISK != None:
        fnames = window.hooks['getAtariDiskDirectory'](ATARI_DISK)
        ata_font = gui_font.Font(family=ATARI_FONTNAME, size=16)
        TEMP_TEXT(window, "\n".join(fnames), os.path.basename(CURRENT_ATARI_DISK_FNAME), bg=ATARI_BLUE, fg=ATARI_WHITE, font=ata_font, width=ATARI_DIR_NB_COLS)
    else:
        gui_mb.showerror("Atari i/o error", "no Atari disk mounted!")
        
def cmdAtariVerboseFileList(window):
    if ATARI_DISK != None:
        fnames = window.hooks['getAtariDiskVerboseDirectory'](ATARI_DISK)
        ata_font = gui_font.Font(family=ATARI_FONTNAME, size=16)
        TEMP_TEXT(window, fnames, os.path.basename(CURRENT_ATARI_DISK_FNAME), bg=ATARI_BLUE, fg=ATARI_WHITE, font=ata_font, width=ATARI_DIR_VB_NB_COLS)
    else:
        gui_mb.showerror("Atari i/o error", "no Atari disk mounted!")
        
def cmdLoadAtariFile(window):
    global CURRENT_ATARI_FILENAME
    if ATARI_DISK != None:
        fname = gui_sd.askstring(os.path.basename(CURRENT_ATARI_DISK_FNAME), "Enter name of credits text to load", initialvalue=CURRENT_ATARI_FILENAME)
        if fname == None or fname == '':
            return
        if fname in window.hooks['getAtariDiskDirectory'](ATARI_DISK):
            CURRENT_ATARI_FILENAME = fname
            text = window.hooks['screencodeToUnicode'](ATARI_DISK.readFile(fname))
            setAtariText(window.ata_window.ata_editor, text)
        else:
            gui_mb.showerror("Atari i/o error", "file %s not found!"%fname, parent=window)
    else:
        gui_mb.showerror("Atari i/o error", "no Atari disk mounted!")

# TODO: finish... or not
#~ def cmdLoadAtariTextFile(window):
    #~ global CURRENT_ATARI_FILENAME
    #~ if ATARI_DISK != None:
        #~ fname = gui_sd.askstring(os.path.basename(CURRENT_ATARI_DISK_FNAME), "Enter name of text file to load", initialvalue=CURRENT_ATARI_FILENAME)
        #~ if fname == None or fname == '':
            #~ return
        #~ if fname in window.hooks['getAtariDiskDirectory'](ATARI_DISK):
            #~ CURRENT_ATARI_FILENAME = fname
            #~ text = window.hooks['screencodeToUnicode'](ATARI_DISK.readFile(fname))
            #~ setAtariText(window.ata_window.ata_editor, text)
        #~ else:
            #~ gui_mb.showerror("Atari i/o error", "file %s not found!"%fname, parent=window)
    #~ else:
        #~ gui_mb.showerror("Atari i/o error", "no Atari disk mounted!")

def cmdSaveAtariFile(window):
    global CURRENT_ATARI_FILENAME
    if ATARI_DISK != None:
        fname = gui_sd.askstring(os.path.basename(CURRENT_ATARI_DISK_FNAME), "Enter name of credits text to save", initialvalue=CURRENT_ATARI_FILENAME)
        if fname == None or fname == '':
            return
        if fname in window.hooks['getAtariDiskDirectory'](ATARI_DISK):
            if not gui_mb.askyesno("Atari i/o warning", "file %s already exists! replace?"%fname, parent=window):
                return
        
        text = window.ata_window.ata_editor.get('1.0', 'end')
        lines = text.split("\n")
        ata_text = str()
        for line in lines:
            line = window.hooks['unicodeToScreencode'](line[LEFT_MARGIN:])
            ata_text += line
        ATARI_DISK.writeFile(fname, ata_text)
    else:
        gui_mb.showerror("Atari i/o error", "no Atari disk mounted!")
            
def cmdDebugConfig(window):
    sys.stdout.write("-------------------------------------------\n")
    sys.stdout.write("CURRENT_FILE_FNAME %s\n"%CURRENT_FILE_FNAME)
    sys.stdout.write("CURRENT_ATARI_DISK_FNAME %s\n"%CURRENT_ATARI_DISK_FNAME)
    sys.stdout.write("ATARI_DISK %s\n"%str(ATARI_DISK))

def cmdDebugNewCredits(window):
    shutil.copyfile("/home/pfeuh/TITREUSE", "/home/pfeuh/CREDITS")

def cmdDebugDumpAtariScreen(window):
    global CURRENT_ATARI_FILENAME
    if ATARI_DISK != None:
        fname = gui_sd.askstring(os.path.basename(CURRENT_ATARI_DISK_FNAME), "Enter name of credits text to load", initialvalue=CURRENT_ATARI_FILENAME)
        if fname == None or fname == '':
            return
        if fname in window.hooks['getAtariDiskDirectory'](ATARI_DISK):
            sys.stdout.write(dump.dump(ATARI_DISK.readFile(fname), nb_columns=40))
        else:
            gui_mb.showerror("Atari i/o error", "file %s not found!"%fname, parent=window)
    else:
        gui_mb.showerror("Atari i/o error", "no Atari disk mounted!")


def getMenu(window):
    menu = gui.Menu(window, fg="white", bg="black")

    # MENU FILES
    menufile = gui.Menu(tearoff=0)
    menufile.add_command(label="New", command=lambda window=window:cmdNew(window))
    menufile.add_command(label="Load", command=lambda window=window:cmdLoad(window))
    menufile.add_command(label="Save", command=lambda window=window:cmdSave(window))
    menufile.add_command(label="Save as...", command=lambda window=window:cmdSaveAs(window))
    menufile.add_command(label="Save copy as...", command=lambda window=window:cmdSaveCopyAs(window))
    
    menufile.add_separator()
    menufile.add_command(label="Quit", command=lambda window=window:cmdQuit(window))
    menu.add_cascade(label="Files", menu=menufile)

    menupref = gui.Menu(tearoff=0)
    menupref.add_command(label="Accentuated")
    menupref.add_command(label="Graphic")
    menu.add_cascade(label="Preferences", menu=menupref)

    menuata = gui.Menu(tearoff=0)
    menuata.add_command(label="Refresh screen", command=lambda window=window:cmdRefreshAtariScreen(window))
    menuata.add_separator()
    menuata.add_command(label="Mount disk", command=lambda window=window:cmdAtariMountDisk(window))
    menuata.add_command(label="Create disk", command=lambda window=window:cmdAtariCreateDisk(window))
    menuata.add_separator()
    menuata.add_command(label="Directory", command=lambda window=window:cmdAtariFileList(window))
    menuata.add_command(label="Verbose directory", command=lambda window=window:cmdAtariVerboseFileList(window))
    menuata.add_separator()
    menuata.add_command(label="Load file", command=lambda window=window:cmdLoadAtariFile(window))
    #~ menuata.add_command(label="Load textFile", command=lambda window=window:cmdLoadAtariTextFile(window))# TODO: finish... or not
    menuata.add_command(label="Save file", command=lambda window=window:cmdSaveAtariFile(window))
    menu.add_cascade(label="Atari 800", menu=menuata)

    if DEBUG:
        menudbug = gui.Menu(tearoff=0)
        menudbug.add_command(label="Config", command=lambda window=window:cmdDebugConfig(window))
        menudbug.add_command(label="New Atari work disk", command=lambda window=window:cmdDebugNewCredits(window))
        menudbug.add_command(label="Dump Atari screen", command=lambda window=window:cmdDebugDumpAtariScreen(window))
        menu.add_cascade(label="Debug", menu=menudbug)

    return menu
    
def getWindow(hooks):
    window = gui.Tk()
    window.hooks = hooks
    window.config(menu=getMenu(window))
    window.raw_editor = getRawEditor(window)
    window.ata_window = gui.Toplevel(window)
    window.ata_window.title(os.path.splitext(os.path.basename(sys.argv[0]))[0])
    window.ata_window.ata_editor = getAtariEditor(window.ata_window)
    loadConf(window)
    return window

if __name__ == "__main__":

    pass
    