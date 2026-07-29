import array as arr

basket1 = {'apple', 'banana', 'mango', 'apple', 'grape'}
basket2 = {'mango', 'kiwi', 'banana', 'kiwi'}
print('this is basket 1',basket1, 'and this is basket 2',basket2)

basket1.add('orange')
print('this is the new basket 1 ',basket1)

commfruit = basket1.intersection(basket2)
print('These are the common fruits in both baskets',commfruit)


fruit_count = arr.array('i',[3,5,2,4])
print(fruit_count)

fruit_count.insert(0,1)
fruit_count.append(7)
print('Fruit count after add and appending items', fruit_count)
print('Number of times 4 appears', fruit_count.count(4),'time(s)')
print('Reverse of fruit count array is', fruit_count.reverse())

print("")

print("===== CLASS FRUIT BASKET ORGANIZER =====")

print("Basket 1:", basket1)

print("Basket 2:", basket2)

print("Shared fruits:", commfruit)

print("Fruit counts:", fruit_count)

print("===========================================")