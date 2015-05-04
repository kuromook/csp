#!/usr/bin/python
# encoding: utf-8

import  os
import sys
from convertCspText import splitLine

if os.name is 'posix':
	# for mac OS
	sys.path.append(os.path.expanduser("~/code/py/csp/"))	
	from copy_paste import pbpaste, pbcopy

	text = pbpaste()
	text = splitLine(text, use_mecab=True)
	pbcopy(text)
else:
	# fow windows
	sys.path.append(os.path.expanduser("~/py/csp/"))
	from tkinter import Tk
	root = Tk()
	root.withdraw()
	text = root.clipboard_get()
	text = splitLine(text, use_mecab=False)
	print(text)
	root.clipboard_append(text)
	root.mainloop()