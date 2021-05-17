#moves zeros to the end of the inputed list
def moveZeros(givenList):
    for num in givenList:
        if num == 0:
            givenList.remove(0)
            givenList.append(0)
    return givenList
