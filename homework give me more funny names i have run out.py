def calculate_circumference():
    radius = float(input('Enter the radius of the circle in cm: '))
    diameter = radius * 2
    pi = 3.141
    circumference = diameter * pi
    print(f'The circumference of the circle is: {circumference} cm')
calculate_circumference()