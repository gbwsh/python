import re, pprint
wordRe = re.compile(r'\w*')
textReDic = {}
def wordCount(text): #use this function
    textRe = wordRe.findall(text)
    for word in textRe:
        if word in textReDic.keys():
            textReDic[word] += 1
        if word != '':
            textReDic.setdefault(word, 1)
    pprint.pprint(textReDic)
