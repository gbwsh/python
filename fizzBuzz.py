def fizzBuzz(num):
    for i in range(1, num + 1):
        output = ''
        if i % 3 == 0:
            output += 'Fizz'
        if i % 5 == 0:
            output += 'Buzz'
        if i % 3 != 0 and i % 5 != 0:
            output += str(i)
        print(output)