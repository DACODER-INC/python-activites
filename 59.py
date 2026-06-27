valid = False
while not valid:
    try:
        number = int(input('Enter a number: '))
        while number % 2 == 0:
            print('BYE')
        valid = True
    except ValueError:
        print('Invalid')