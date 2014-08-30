#!/usr/bin/python
# encoding: utf-8

import sys, os
sys.path.append(os.path.expanduser("~/code/py/csp/"))

if os.name is 'posix':
    from copy_paste import pbpaste, pbcopy
    from convertCspText import convertCspText
    text = pbpaste()
    text = convertCspText(text)
    pbcopy(text)
else:
    print "error"