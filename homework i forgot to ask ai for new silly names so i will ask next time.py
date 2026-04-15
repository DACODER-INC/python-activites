decimal_num = float(input('Enter a decimal number that can be converted to a binary number: '))
binary_num = ''
while decimal_num > 0:
    remainder = int(decimal_num % 2)
    binary_num = str(remainder) + binary_num
    decimal_num //= 2
print(f'The binary representation of the decimal number is: {binary_num}')
