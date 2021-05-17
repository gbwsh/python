def printTabs(TABS):
    for e in range(1 ,7):
        print('--'.join(tabs['string' + str(e)]))

while True:
    strings = []
    tabs = {}
    for q in range(1, 7):
        print('Enter string number ' + str(q) + ':')
        string = input()
        strings.append(string)
        tabs.setdefault('string' + str(q), [strings[q-1] + '|'])
    answer = input('Type Y if you\'ve inputed them correctly:\n')
    if answer.lower() == 'y':
        break
    else:
        continue

for i in range(1, 101): 
    printTabs(tabs)
    print('What frets would you like to add in slot number ' + str(i))
    for r in range(1, 7):
        note = input('for string ' + tabs['string' + str(r)][0] + ':\n')
        if note == '':
            note = '-'
        tabs['string' + str(r)].append(note)