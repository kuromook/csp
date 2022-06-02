#!/usr/bin/python
# encoding: utf-8

from convertCspText import splitLine
with open("source.txt", 'r',encoding='utf8') as f:
    data = f.readlines()

f= open("out.txt","w+")
f.write(splitLine(''.join(data)))
f.close()
