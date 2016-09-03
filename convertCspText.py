#!/usr/bin/python
# encoding: utf-8

""" convert scenario text string to speaking text of story editor
on clip studio paint
"""

row_separator_source = '\n\n\n'
row_separator_converted = "\np\n"

speak_separator_source_win = '\r\n\r\n'
speak_separator_source_mac = '\n\n'
speak_separator_converted = "\nl\n"


def split_str_mecab(string, return_num=24):
    'split speak by mecab'
    import MeCab
    mecab = MeCab.Tagger("mecabrc")
    mecab.parse('')  # for MeCab bug
    encoded = string  # for MeCab bug
    node = mecab.parseToNode(encoded)

    speakCount = 0
    speak = ""

    while node:
        c = node.surface
        p = node.feature.split(',')[0]

        if speakCount > return_num and (p == '助詞'):
            speak = speak + c + "\n"
            speakCount = 0
        elif speakCount > return_num and (c == '…'):
            speak = speak + c + "\n"
            speakCount = 0
        else:
            speak = speak + c
            speakCount += node.length
        node = node.next

    return speak + "\n"


def split_str(s, return_num=10):
    "speak return by its length 10"
    length = len(s)
    return [s[i:i+return_num] for i in range(0, length, return_num)]


def splitPage(string, use_mecab=True):
    ary = string.split(row_separator_source)
    reary = [splitLine(v, use_mecab) for v in ary]
    return row_separator_converted.join(reary)


def splitLine(string, use_mecab=True):
    import os
    sep = speak_separator_source_mac if os.name is 'posix' else speak_separator_source_win
    ary = string.split(sep)
    reary = [convertCspText(v, use_mecab) for v in ary]
    return speak_separator_converted.join(reary)


def convertCspText(string, use_mecab=True):
    speakingSeparator = "\n\n"

    ary = []
    speak = ""

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

        if(pair["think"]["flag"] or pair["speak"]["flag"] or pair["monologue"]["flag"]):
            speak = speak + c

        for v in pair.values():
            if c == v["pre"]:
                v["flag"] = True

    if not use_mecab:
        ary = ["\n".join(split_str(v)) for v in ary]
    else:
        ary = [split_str_mecab(v) for v in ary]

    return speakingSeparator.join(ary)
