#!/usr/bin/python
# encoding: utf-8


import MeCab
texts = "「明日は(晴れる)か<な>」"
mecab = MeCab.Tagger("mecabrc")
data = []
data.append(texts)
node = mecab.parseToNode(texts)
while node:
    print node.surface,":", node.feature.split(',')[0], node.feature.split(',')[1]
    node = node.next