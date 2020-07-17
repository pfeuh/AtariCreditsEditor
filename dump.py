#!/usr/bin/python
# -*- coding: utf-8 -*-

UNPRINTABLE_CHAR = "."

def byteToPrintable(byte):
    if byte < 32:
        return UNPRINTABLE_CHAR
    elif byte > 127:
        return UNPRINTABLE_CHAR
    else:
        return chr(byte)

def dump(bytes, nb_columns=16):
    if nb_columns < 1:
        raise Exception("Bad number of columns! Expected >= 1 got %i!"%nb_columns)
    max_column_number = nb_columns - 1
    index = 0
    ascii_buf = ""
    text = ""
    for index in range(len(bytes)):
        if (index % nb_columns) == 0:
            text += "%04X : "%index
            ascii_buf = ""
            
        value = bytes[index]
        if type(value) == str:
            value = ord(value)
        elif type(value) == unicode:
            value = ord(value)
        if value & 0xff != value:
            raise Exception("at position %04x Expected value in 0x00-0xff - got %i!"%(index, value))
        text += "%02X "%value
        ascii_buf += byteToPrintable(value)
        
        if (index % nb_columns) == max_column_number:
            text += ascii_buf
            text += "\n"
            
    if (index % nb_columns) != max_column_number:
        while (index % nb_columns) != max_column_number:
            text += "   "
            index += 1
        text += ascii_buf
        text += "\n"
    return text

def dumpUnicode(bytes, nb_columns=16):
    if nb_columns < 1:
        raise Exception("Bad number of columns! Expected >= 1 got %i!"%nb_columns)
    max_column_number = nb_columns - 1
    index = 0
    ascii_buf = ""
    text = ""
    for index in range(len(bytes)):
        if (index % nb_columns) == 0:
            text += "%04X : "%index
            ascii_buf = ""
            
        value = bytes[index]
        if type(value) == str:
            value = ord(value)
        elif type(value) == unicode:
            value = ord(value)
        #~ if value & 0xff != value:
            #~ raise Exception("at position %04x Expected value in 0x00-0xff - got %i!"%(index, value))
        text += "%04X "%value
        ascii_buf += byteToPrintable(value)
        
        if (index % nb_columns) == max_column_number:
            text += ascii_buf
            text += "\n"
            
    if (index % nb_columns) != max_column_number:
        while (index % nb_columns) != max_column_number:
            text += "     "
            index += 1
        text += ascii_buf
        text += "\n"
    return text

if __name__ == "__main__":
    
    import sys

    sys.stdout.write(dumpUnicode([x for x in range(123)]))
    sys.stdout.write(dumpUnicode([x for x in range(123)], 16))
    sys.stdout.write(dumpUnicode([x for x in range(65, 80)], 1))
    
    