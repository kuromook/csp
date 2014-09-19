#!/usr/bin/python
# encoding: utf-8

""" convert scenario text string to speaking text of story editor
on clip studio paint
"""

def splitPage(string):
    ary = string.split('\n\n\n')
    reary = []
    for v in ary:
        reary.append(splitLine(v))

    return "\np\n".join(reary)


def splitLine(string):
    ary = string.split('\n\n')
    reary = []
    for v in ary:
        reary.append(convertCspTextByMecab(v))

    return "\nl\n".join(reary)


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
