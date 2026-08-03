items = ['apple watch', 'iphone', 'ipad', 'macbook pro','macbook air', 'macbook neo','apple pencil','magic keyboard for ipad','magic keyboard for imac and magic mouse for imac bundle', 'imac']
stock_counts = [78, 500, 450, 2000, 2000, 0, 300, 300, 600, 1000]

inventory = {item:count for item, count in zip(items, stock_counts)}
print('Full inventory is', inventory)

in_stock_items = [item for item in items if inventory[item] > 0]
print('\n the items in stock are ', in_stock_items)

picked_items = input('Which item do you want to buy?')
if picked_items not in inventory or inventory[picked_items] == 0:
    print('chosen item is either out of stock or doesnt exit so i am stopping the checker')
    exit()


prices = [329, 1499, 1768, 2399, 1299, 949, 179, 449, 250, 1499]
markup = int(input('Enter the markup amount'))
markup_prices = list(map(lambda p:p+markup, prices))
print('List with marked up prices',markup_prices)


item_index = items.index(picked_items)
chosen_price = markup_prices[item_index]
print('\n price of chosen item after markup is ', chosen_price)


inventory[picked_items] = inventory[picked_items] -1
print(picked_items, 'going to check out. remaining stock :', inventory[picked_items])


card_num = int(input('Enter your 16 digit card number'))
name_card = input('Enter the full name on the card ')
your_name = input('Enter your full name ')
if name_card == your_name:
    pass
else:
    print('The name doesnt match ')
    exit()

cvv = int(input('Enter you cvv'))
exp_date = input('Enter the exp date in this format mm/yyyy')
print('Purchase completed, Welcome to the Apple ecosystem')


print("")

print("===== APPLE STORE INVENTORY CHECKER =====")

print("Item Bought:", picked_items)

print("Price Paid:", chosen_price)

print("Updated Inventory:", inventory)

print("=============================================")
