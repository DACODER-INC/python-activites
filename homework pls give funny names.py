snack_box1 = {"chips", "juice", "cookies", "chips", "apple"}
snack_box2 = {"cookies", "sandwich", "juice", "sandwich"}
print("Snack Box 1:", snack_box1)
print("Snack Box 2:", snack_box2)


snack_box1.add('banana')
print('This the updated snack box 1', snack_box1)

common_snacks = snack_box1.intersection(snack_box2)
print('These are the snacks in both boxes', common_snacks)

import array as arr
snack_counts = arr.array('i', [4, 5, 3, 9])
print('Snack counts array', snack_counts)

snack_counts.insert(2, 5)
snack_counts.append(7)
print('The updated snack count array', snack_counts)


count_of_5 = snack_counts.count(5)
print('This is how many times 5 appeared in snack counts', count_of_5)


snack_counts.reverse()
print('This is the reversed snack count', snack_counts)

print("")
print("===== SCHOOL SNACK COUNTER =====")
print("Snack Box 1:", snack_box1)
print("Snack Box 2:", snack_box2)
print("Shared snacks:", common_snacks)
print("Snack counts:", snack_counts)
print("================================")