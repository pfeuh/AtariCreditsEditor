#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

# TODO: there is a bug in justifying both sides... Often just before last line
# TODO: Make some tests on SCREEN_COLS

EMPTY = ""
CHAR_SPACE = " "
CHAR_UNDERSCORE = "_"
CHAR_LF = "\n"
CHAR_CR = "\r"
CHAR_TAB = "\t"
CHAR_SHARP = "#"
PATTERN_TAB = CHAR_SHARP + "TAB" + CHAR_SHARP
PATTERN_LEFT = CHAR_SHARP + "LEFT" + CHAR_SHARP
PATTERN_RIGHT = CHAR_SHARP + "RIGHT" + CHAR_SHARP
PATTERN_CENTER = CHAR_SHARP + "CENTER" + CHAR_SHARP
PATTERN_JUSTIFIED = CHAR_SHARP + "JUSTIFY" + CHAR_SHARP

FORMAT_LEFT = 1
FORMAT_RIGHT = 2
FORMAT_CENTER = 3
FORMAT_JUSTIFY = 4

DEBUG = "-debug" in sys.argv
SCREEN_COLS = 40
SCREEN_ROWS = 25
SCREEN_TAB = 4

for index, arg in enumerate(sys.argv):
    if arg == "-nb_cols":
        SCREEN_COLS = int(sys.argv[index+1])

def getNbCols():
    return SCREEN_COLS

class LINE():
    def __init__(self, text=None):
        self.__mode = FORMAT_LEFT
        self.__words = []
        if text != None:
            text = text.replace(CHAR_CR, EMPTY)
            if "\<>" in text:
                text = text.replace("\<>", EMPTY)
                self.__mode = FORMAT_JUSTIFY
            if "\><" in text:
                text = text.replace("\><", EMPTY)
                self.__mode = FORMAT_CENTER
            if "\<" in text:
                text = text.replace("\<", EMPTY)
                self.__mode = FORMAT_LEFT
            if "\>" in text:
                text = text.replace("\>", EMPTY)
                self.__mode = FORMAT_RIGHT

            if self.__mode in (FORMAT_LEFT, FORMAT_JUSTIFY):
                text = text.replace(CHAR_TAB, CHAR_SPACE + PATTERN_TAB + CHAR_SPACE)
            else:
                text = text.replace(CHAR_TAB, EMPTY)
            
            text= text.strip()
            words = [word.strip() for word in text.split()]
            for word in words:
                if word == PATTERN_LEFT:
                    pass
                elif word == PATTERN_RIGHT:
                    pass
                elif word == PATTERN_CENTER:
                    pass
                elif word == PATTERN_JUSTIFIED:
                    pass
                else:
                    self.__words.append(word)

    def adjustLeft(self, text, cols=SCREEN_COLS):
        new_text = EMPTY
        words = text.split()
        for word in words:
            if word == PATTERN_TAB:
                new_text += CHAR_SPACE
                while len(new_text) % SCREEN_TAB:
                    new_text += CHAR_SPACE
            else:
                new_text += word
                if len(new_text) % cols:
                    new_text += CHAR_SPACE
        
        while len(new_text) % cols:
            new_text += CHAR_SPACE
        return new_text
    
    def adjustRight(self, text, cols=SCREEN_COLS):
        while len(text) % cols:
            text = CHAR_SPACE + text
        return text
    
    def adjustCenter(self, text, cols=SCREEN_COLS):
        while len(text) % cols:
            text = CHAR_SPACE + text
            if len(text) < cols:
                text += CHAR_SPACE
        return text
    
    def adjustJustify(self, text, cols=SCREEN_COLS):
        words = text.split()
        len_words = sum([len(word) for word in words])
        nb_seps = len(words) - 1
        seps = [1] * nb_seps
        len_seps = nb_seps
        index = 0
        while len_words + len_seps < cols:
            seps[index] += 1
            len_seps += 1
            index = (index + 1) % nb_seps
            text = CHAR_SPACE + text
        text = words[0]
        for index in range(nb_seps):
            text += CHAR_SPACE * seps[index] + words[index + 1]
        return text

    def adjustLineSize(self, text, cols=SCREEN_COLS, mode=None, tab=SCREEN_TAB):
        if mode == None:
            mode = self.__mode
        
        if mode == FORMAT_LEFT:
            out_text = self.adjustLeft(text, cols)
        elif mode == FORMAT_RIGHT:
            out_text = self.adjustRight(text, cols)
        elif mode == FORMAT_CENTER:
            out_text = self.adjustCenter(text, cols)
        elif mode == FORMAT_JUSTIFY:
            out_text = self.adjustJustify(text, cols)
        else:
            raise Exception("Unexpected internal error!\nmode = %d"%str(mode))
            
        #~ if len(out_text) != cols:
        if len(out_text) % cols:
            raise Exception("Unexpected bad size for string\n<%s>\n expected %d got %s"%(out_text, cols, len(out_text)))
        return out_text

    def getFormatedText(self, cols=SCREEN_COLS, tab=SCREEN_TAB):
        formated_text = EMPTY

        current_line = EMPTY
        last_wnum = len(self.__words) -1
        for wnum, word in enumerate(self.__words):
            mode = self.__mode
            if current_line != EMPTY:
                space = CHAR_SPACE
            else:
                space = EMPTY

            if len(word) + len(current_line) + len(space) > cols:
                if wnum == last_wnum:
                    mode = FORMAT_LEFT
                formated_text += self.adjustLineSize(current_line, cols, mode, tab)
                current_line = word
            else:
                current_line += space + word

        if current_line != EMPTY:
            mode = self.__mode
            if self.__mode == FORMAT_JUSTIFY:
                mode = FORMAT_LEFT
            formated_text += self.adjustLineSize(current_line, cols, mode, tab)

        if formated_text == EMPTY:
            formated_text = CHAR_SPACE * cols
            
        return formated_text

    def getWords(self):
        return self.__words
            
    def getMode(self):
        return self.__mode
            
    def __str__(self):
        return "%u %s"%(self.__mode, str(self.__words))

class TEXT_BUFFER():
    def __init__(self, text=None, cols=SCREEN_COLS, rows=SCREEN_ROWS, tab=SCREEN_TAB):
        self.__cols = cols
        self.__rows = rows # TODO: can delete, not used
        self.__tab = tab
        self.clear()
        if text != None:
            self.addText(text)

    def clear(self):
        self.__lines = []
        self.__current_mode = FORMAT_LEFT
        
    def getWords(self):
        return self.__words

    def addText(self, text):
        lines = text.split(CHAR_LF)
        for line in lines:
            self.__lines.append(LINE(line))

    def getFormatedText(self):
        text_buffer = EMPTY
        for line in self.__lines:
            text_buffer += line.getFormatedText(self.__cols, self.__tab)
        text_buffer = text_buffer.replace(CHAR_UNDERSCORE, CHAR_SPACE)
        return text_buffer

    def getLines(self):
        return self.__lines

    def __str__(self):
        text = EMPTY
        line_num = 0
        screen_text = self.getFormatedText()
        
        while 1:
            line = screen_text[line_num * self.__cols:(line_num + 1) * self.__cols]
            text += "|" + line + "|" + CHAR_LF
            line_num += 1
            if (line_num * self.__cols) >= len(screen_text):
                break
        return text

if __name__ == "__main__":

    text = open("./text/utest.utf").read(-1).decode("utf-8")
    buf = TEXT_BUFFER(text)
    sys.stdout.write(buf.getFormatedText())

    