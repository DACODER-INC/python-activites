def calculate_change(bill, payment):
    return payment - bill

bill = int(input('Enter the amount of the bill: '))
payment = int(input('Enter the amount you want to pay 5, 10, 20, 50, 100, 200, 500, 1000: '))
 

change = calculate_change(bill, payment)
print(f'The change is: {change}')