# Initialize dictionary

test_dict = {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}

print(test_dict)

k = int(input('what number do you want to check for:'))
frequency = 0
for key in test_dict:
    if test_dict[key] == k:
        frequency = frequency + 1


print(frequency)
