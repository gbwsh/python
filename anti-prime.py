'''This code searches for the highest composite number starting with
the highest listed on wikipedia. mostDivisorsList shows the full list
of divisors for the most composite number while mostDivisorsNumber
shows the number and the amount of divisors respectively in a dictionary'''
checkedNumber=1
divisorNumber=1
currentDivisorsList = []
mostDivisorsList = []
mostDivisorsNumber = {}
mostComplexNumber = 0
while True:
    try:
        if checkedNumber%divisorNumber==0:
            #print(divisorNumber)
            currentDivisorsList.append(divisorNumber)
            if checkedNumber==divisorNumber:
                #print("Above was counted for " + str(checkedNumber))
                divisorNumber=1
                if len(currentDivisorsList)>len(mostDivisorsList):
                    mostDivisorsList = currentDivisorsList
                    mostDivisorsNumber = {}
                    mostDivisorsNumber.setdefault(checkedNumber, len(mostDivisorsList))
                    mostComplexNumber = checkedNumber
                    print(mostComplexNumber)
                currentDivisorsList=[]
                checkedNumber+=1
            divisorNumber+=1
        else:
            divisorNumber+=1
    except KeyboardInterrupt:
            print('Counting stopped...\nCurrent most complex number is... '
                  + str(mostComplexNumber) + '\nIt has... '
                  + str(mostDivisorsNumber[mostComplexNumber])
                  + ' divisors\nThe list of it\'s divisors is stored under: mostDivisorsList.')
            break
