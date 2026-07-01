try:
    age = int(input('Enter your age to get a drivers license: '))
    if age < 19:
        raise ValueError('You are not eligible to get a drivers license')
    else:
        print('You are eligible to get a drivers license, please go to the nearest DMV office to apply for your license')
except ValueError as e:
    print(e)
finally:  
    if age % 2 == 0:
        print('Your age is even')
    else:
        print('Your age is odd')