#!/usr/bin/python
# -*- coding: utf-8 -*- 
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
	sys.path.append(os.path.expanduser("~/../../py/csp/"))
	import clipboard
	text = clipboard.paste()
	if not text:
		# for in use emacs call-process-region, but not work 
		import sys
		import codecs
		sys.stdin  = codecs.getreader('utf8')(sys.stdin)
		text = sys.stdin.read()

	text = splitLine(text, use_mecab=False)
	clipboard.copy(text)
