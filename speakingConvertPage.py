#!/usr/bin/python
# encoding: utf-8

import sys
import os
sys.path.append(os.path.expanduser("~/code/py/csp/"))

if os.name == 'posix':
    from copy_paste import pbpaste, pbcopy
    #from convertCspText import convertCspText
    from convertCspText import splitLine
    #from convertCspText import convertCspTextByMecab

    text = pbpaste()
    text = splitLine(text)
    pbcopy(text)
else:
    print(error)