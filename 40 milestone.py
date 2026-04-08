minimum = int(input('Enter a minimum number: '))
maximum = int(input('Enter a maximum number: '))
for num in range(minimum, maximum + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print('The prime numbers between', minimum, 'and', maximum, 'are:', num)
