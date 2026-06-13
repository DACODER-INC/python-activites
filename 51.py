def total_tip(bill_amount, tip_perc):
    total = bill_amount * (1 + tip_perc * 0.01)
    return total
total_bill_amount = total_tip(150, 15)
print('please pay:', total_bill_amount)
card_number = (input('Enter your card number:'))
expiry_date = input('Enter the expiry date (MM/YY):')
cvv = int(input("Enter the CVV:"))
print("Payment successful! Thank you for your purchase.")
