string = str(input('Enter a word: '))
letter = str(input('Enter a letter to check if it is in the word and if so, how many times it appears: '))
count = 0
i = 0
while i < len(string):
    if string[i] == letter:
        count += 1
    i += 1
if count > 0:
    print(f'The letter "{letter}" appears in the word "{string}" {count} times.')
else:
    print(f'The letter "{letter}" does not appear in the word "{string}".')