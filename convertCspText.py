#!/usr/bin/python
# encoding: utf-8

""" convert scenario text string to speaking text of story editor
on clip studio paint
"""

def convertCspText(string):
    speakingSeparator = "\n\n"

    ary = []
    speak = ""

    pair = {
        "think": {"pre": u"(", "suff": u")", "flag": False},
        "speak": {"pre": u"「", "suff": u"」", "flag": False},
        "monologue": {"pre": u"<", u"suff": ">", "flag": False}
        }

    for c in string:
        for v in pair.itervalues():
            if (v["flag"] and c == v["suff"]):
                v["flag"] = False
                speak += "\n"
                ary.append(speak)
                speak = ""
        
        if(pair["think"]["flag"] or pair["speak"]["flag"] or pair["monologue"]["flag"]):
            speak = speak + c

        for v in pair.itervalues():
            if c == v["pre"]:
                v["flag"] = True

    return speakingSeparator.join(ary)

