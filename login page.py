while True:
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    if username == 'Nav' and password == 'password123':
        print('enter the answer to your security question to login')
        security_answer = input('What is your debit card provider? ')
        if security_answer.lower() == 'mydoh and visa':
            print('Login successful! Welcome, Nav!')
        else:
            print('Incorrect username, password, or security answer. Access denied.')

