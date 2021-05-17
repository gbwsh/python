#wordCount function uses regex to iterate over each word in a given string
#and prints out how many times each word has been used, case insensitive

import re, pprint
wordRe = re.compile(r'\w*')

def wordCount(text):
    textReDic = {}
    textRe = wordRe.findall(text)
    for word in textRe:
        if word.lower() in textReDic.keys():
            textReDic[word.lower()] += 1
        if word != '':
            textReDic.setdefault(word.lower(), 1)
    for k, v in textReDic.items():
        print(k +': '+ str(v))
