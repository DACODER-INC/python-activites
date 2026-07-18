def palindrome(word):
    e = len(word) - 1
    s = 0
    while (s < e):
        if (word[s]!= word[e]):
            return False

        s += 1
        e -= 1
    return True



r = ('level')
if (palindrome(r)):
    print('Tuple is a palindrome')
else:
    print('Tuple is not a palindrome')