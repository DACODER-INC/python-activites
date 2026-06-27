try:
    num1, num2 = eval(input('Enter two numbers seperated by a comma: '))
    result = num1 / num2
    print('The result is ', result)
except ZeroDivisionError:
    print('Division by zero is impossible')
except SyntaxError:
    print('Comma is missing please enter 2 numbers sperated by a comma like this 1, 2')
except:
    print('Wrong input')
else:
    print('No exceptions occured')
finally:
    print('This statement will always be excecuted no matter what')