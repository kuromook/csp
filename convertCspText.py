#!/usr/bin/python
# encoding: utf-8

""" convert scenario text string to speaking text of story editor
on clip studio paint
"""

""" old version ( not used )"""
def convertCspText(string):
    speakingSeparator = "\n\n"

    isCarregeReturnPrevious = False
    ary = []
    speak = ""
    speakCount = 0

    pair = {
        "think": {"pre": u"(", "suff": u")", "flag": False},
        "speak": {"pre": u"「", "suff": u"」", "flag": False},
        "monologue": {"pre": u"<", u"suff": ">", "flag": False}
        }

    for c in string:
        for v in pair.values():
            if (v["flag"] and c == v["suff"]):
                v["flag"] = False
                speak += "\n"
                ary.append(speak)
                speak = ""
                speakCount = 0

        if any([v["flag"] for v in pair.values()]):
            if speakCount > 10 and (c == u"、" or c == u"\n"):
                speak = speak + u"\n"
                speakCount = 0
            else:
                speak = speak + c
                speakCount += 1

        for v in pair.values():
            if c == v["pre"] and isCarregeReturnPrevious:
                v["flag"] = True

        if c == '\n':
            isCarregeReturnPrevious = True
        else:
            isCarregeReturnPrevious = False

    return speakingSeparator.join(ary)

""" current version """
def convertCspTextByMecab(string):
    speakingSeparator = "\n\n"

    ary = []
    speak = ""
    speakCount = 0
    
    import MeCab
    mecab = MeCab.Tagger("mecabrc")
    encoded = string.encode('utf-8')
    node = mecab.parseToNode(encoded)

    pair = {
        "think": {"pre": "(", "suff": ")", "flag": False},
        "speak": {"pre": "「", "suff": "」", "flag": False},
        "monologue": {"pre": "<", "suff": ">", "flag": False}
        }

    while node:
        c = node.surface
        p = node.feature.split(',')[0]

        for v in pair.values():
            if (v["flag"] and c == v["suff"]):
                v["flag"] = False
                speak += "\n"
                ary.append(speak.decode('utf-8'))
                speak = ""
                speakCount = 0

        if any([v["flag"] for v in pair.values()]):
            if speakCount > 20 and (c == "、" or c == "\n"):
                speak = speak + "\n"
                speakCount = 0
            elif speakCount > 30 and (p == '助詞'):
                speak = speak + c + "\n"
                speakCount = node.length
            else:
                speak = speak + c
                speakCount += node.length

        for v in pair.values():
            if c == v["pre"]:
                v["flag"] = True


        node = node.next

    return speakingSeparator.join(ary)
