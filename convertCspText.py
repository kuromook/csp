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


def splitPage(string, use_mecab=True):
    ary = string.split(row_separator_source)
    reary = [splitLine(v, use_mecab) for v in ary]
    return row_separator_converted.join(reary)


def splitLine(string, use_mecab=True):
    import os
    sep = speak_separator_source_mac if os.name is 'posix' else speak_separator_source_win
    ary = string.split(sep)
    reary = [convertCspText(v, use_mecab) for v in ary]
    #func = convertCspTextByMecab if use_mecab else convertCspText
    #reary = [func(v) for v in ary]
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

    def split_str(s, n):
        "split string by its length"
        length = len(s)
        return [s[i:i+n] for i in range(0, length, n)]



    def split_str_mecab(string, n):
        import MeCab
        mecab = MeCab.Tagger("mecabrc")
        mecab.parse('')  # これを追記！

        encoded = string
        node = mecab.parseToNode(encoded)
        speakCount = 0
        speak = "" 
        while node:
            c = node.surface
            p = node.feature.split(',')[0]

            if speakCount > 24 and (p == '助詞'):
                speak = speak + c + "\n"
                speakCount = 0
            else:
                speak = speak + c
                speakCount += node.length

            node = node.next

        #print(speak)
        return speak + "\n"

    if not use_mecab:
        ary = ["\n".join(split_str(v, 10)) for v in ary]
    else:
        ary = [split_str_mecab(v, 10) for v in ary] 

    return speakingSeparator.join(ary)

