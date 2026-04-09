num = int(input("Enter a number: "))
num_of_digits = 0
temp = num
while temp > 0:
    temp //= 10
    num_of_digits += 1
print(f"The number of digits in {num} is: {num_of_digits}")
