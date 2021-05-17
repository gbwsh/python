def rot13(message):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    letters = []
    values = {}
    output = ''
    i = 1
    for letter in alph:
        letters.append(letter)
        values.setdefault(letter, i)
        i += 1
    for j in message:
        if j.lower() in values:
            if values[j.lower()]+13 <= 26:
                if j.isupper():
                    output += letters[values[j.lower()]+12].upper()
                else:
                    output += letters[values[j]+12]
            else:
                if j.isupper():
                    output += letters[values[j.lower()]-14].upper()
                else:
                    output += letters[values[j.lower()]-14]
        else:
            output += j
    return output
