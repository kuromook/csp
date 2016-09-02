#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from convertCspText import splitLine, splitPage

if os.name is 'posix':
	sys.path.append(os.path.expanduser("~/code/py/csp/"))
	from copy_paste import pbpaste, pbcopy

	text = pbpaste()
	text = splitLine(text, use_mecab=True)
	pbcopy(text)
else:
	sys.path.append(os.path.expanduser("~/../../py/csp/"))
	import clipboard
	text = clipboard.paste()

	text = splitLine(text, use_mecab=True)
	print(text)
	clipboard.copy(text)
