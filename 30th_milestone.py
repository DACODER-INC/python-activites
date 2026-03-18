elec_units = float(input('Enter your electricity units: '))
if elec_units <= 50:
    amount = (elec_units * 2.60) + 25
elif elec_units <= 100:
    amount = (elec_units * 3.25) + 35
elif elec_units <= 200:
    amount = (elec_units * 5.26) + 45
else:
    amount = (elec_units * 8.45) + 75
print(f'Your electricity bill is: ${amount:.2f}')