def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a*b
def divide(a, b):
    return a/b
operation = str(input('add subtract multiply or divide:'))
num1 = float(input('Enter the first number:'))
num2 = float(input('Enter the second number:'))
if operation == 'add':
    print(add(num1, num2))
elif operation == 'subtract':
    print(subtract(num1, num2))
elif operation == 'multiply':
    print(multiply(num1, num2))
elif operation == 'divide':
    print(divide(num1, num2))

