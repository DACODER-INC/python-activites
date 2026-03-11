char = input("Enter a character: ")
if type(char) == str and len(char) == 1:
	ascii_val = ord(char)


print(f"\nCharacter: '{char}'")
print(f"ASCII Value: {ascii_val}")



print('\nCharacter: ', end='')
if ascii_val >= 65 and ascii_val <= 90:
    print('Uppercase Letter')
elif ascii_val >= 97 and ascii_val <= 122:
    print('Lowercase Letter')
elif ascii_val >= 48 and ascii_val <= 57:
    print('Digit')
elif ascii_val == 32:
    print('Space')
elif ascii_val >= 33 and ascii_val <= 126:
    print('Special Character')
else:
    print('\nInvalid input. Please enter a single character.')
