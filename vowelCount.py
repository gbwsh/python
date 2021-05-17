def countVowels(text):
    vowels = {'a':0,
            'e':0,
            'i':0,
            'o':0,
            'u':0,}
    for letter in text.lower():
        if letter in vowels:
            vowels[letter] += 1
    return vowels
