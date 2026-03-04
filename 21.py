height = float(input('Enter your height in cm: '))
weight = float(input('Enter your weight in kg: '))
BMI = weight / (height / 100) ** 2
print('Your BMI is: ', BMI)

if BMI < 18.5:
    print('You are underweight')
elif 18.5 <= BMI < 25:
    print('You are normal weight')
elif 25 <= BMI < 30:
    print('You are overweight')
elif BMI >= 30:
    print('You are severely overweight')
elif BMI >= 40:
    print('You are obese')
else:
    print('You are severely obese')