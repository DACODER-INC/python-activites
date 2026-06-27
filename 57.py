number = int(input('Enter a number: '))
try:
    print('The number you entered is', number)
except ValueError as ex:
    print('exception', ex)