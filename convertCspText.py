#!/usr/bin/python
# encoding: utf-8

""" convert scenario text string to speaking text of story editor
on clip studio paint
"""

def splitPage(string, use_mecab=True):
    ary = string.split('\n\n\n')
    reary = [splitLine(v, use_mecab) for v in ary]
    return "\np\n".join(reary)


def splitLine(string, use_mecab=True):
    ary = string.split('\n\n')
    if use_mecab:
        func = convertCspTextByMecab
    else:
        func = convertCspText
    reary = [func(v) for v in ary]

    return "\nl\n".join(reary)


"on windows, Mecab-Python does not work fine"
"then use old version "
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
    print(ary)
    return speakingSeparator.join(ary)



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
        "think": {"pre": "(", "suff": ")", "flag": 0},
        "speak": {"pre": "「", "suff": "」", "flag": 0},
        "monologue": {"pre": "<", "suff": ">", "flag": 0},
        "description": {"pre": "[", "suff": "]", "flag": 0}
        }

    while node:
        c = node.surface
        p = node.feature.split(',')[0]

        for k, v in pair.items():
            if c.endswith(v['suff']):
                if v["flag"] == 1:
                    pair["think"]["flag"] = 0
                    pair["speak"]["flag"] = 0
                    pair["monologue"]["flag"] = 0
                    pair["description"]["flag"] = 0

                    speak += c.replace(v['suff'], '')
                    if k is "description":
                        speak = "`" + speak
                    speak += "\n"
                    ary.append(speak.decode('utf-8'))
                    speak = ""
                    speakCount = 0
                else:
                    v["flag"] -= 1

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

        for k, v in pair.items():
            if c.startswith(v["pre"]):
                v["flag"] += 1


        node = node.next

    return speakingSeparator.join(ary)
