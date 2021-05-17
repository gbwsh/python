#outputs a list of characters from a string without having two of the same characters next to eachother
#case sensitive
def uniqueToList(iterable):
    output = []
    for i in range(len(iterable)):
        if output == []:
            output.append(iterable[i])
        elif iterable[i-1] != iterable[i]:
            output.append(iterable[i])
    return output
#examples
uniqueToList('AAAABBBCCDAABBB') # --> ['A', 'B', 'C', 'D', 'A', 'B']
uniqueToList('ABBCcAD')         # --> ['A', 'B', 'C', 'c', 'A', 'D']
uniqueToList([1,2,2,3,3])       # --> [1,2,3]
