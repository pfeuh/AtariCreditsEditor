#!/usr/bin/python
# -*- coding: utf-8 -*-

import atariCreditsEditor as ACE

for index in range(len(ACE.SCREEN_TO_UNICODE)):
    print index, ord(ACE.screenToUnicode(chr(index)))

