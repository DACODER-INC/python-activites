num = int(input(' Enter a number: '))
temp = num
numLen = 0
while temp > 0:
    temp //= 10
    numLen += 1
if numLen >= 4:
    numLen = int(numLen / 2)
    sum = 0
    while num > 0:
        digit = num % 10
        if sum == numLen:
            midOne = digit
        elif sum == numLen - 1:
            midTwo = digit
        num = int(num / 10)
        sum += 1
    tp = midOne * midTwo
    print(f'The product of the middle two digits is: {tp}')
else:
    print('The number does not have an even number of digits.')


    