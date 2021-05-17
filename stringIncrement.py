'''
addNum function adds a 1 to the end of a string if there is no digit there and increments it by 1 if it ends with a number
'''
def addNum(string):
    for char in range(len(string)):
        if string[char].isdigit():
            return string[:char] + str(int(string[char:]) + 1)
    return string + '1'