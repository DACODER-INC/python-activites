real_amount = float(input(' Enter how much you bought the orange for '))
selling_price = float(input( ' Enter how much you sold the orange for'))
if selling_price > real_amount:
    print(' you made a profit of ' + str(selling_price - real_amount))
if selling_price < real_amount:
    print(' you lost ' + str(real_amount - selling_price))
    