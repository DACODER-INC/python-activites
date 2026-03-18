while True:
    med = str(input(" do you have a medical condition. answer with y or n: ").strip().upper())
    if med.isalpha():
        break
    else:
        print('Invalid input. Please enter Y or N.')
if med == 'Y':
    print('You are allowed to take the exam ')
else:
    while True:
        attendance = str(input('How many classes have you attended? '))
        if attendance.isdigit():
            attendance = int(attendance)
            break
        else:
            print('Invalid input. Please enter a number.')
    if attendance >= 75:
        print('You are allowed to take the exam ')
    else:
        print('You are not allowed to take the exam ')