numrows = int(input('Enter the number of rows for a diamond with number of rows: '))
if numrows % 2 == 0:
    halfdiamondrow = int(numrows / 2)
else:  
    halfdiamondrow = int((numrows + 1) / 2)
space = halfdiamondrow - 1
for i in range(halfdiamondrow + 1):
    for j in range(space + 1):
        print(end=" ")
    space -= 1
    num = 1
    for j in range(2 * i - 1):
        print(end=str(num))
        num += 1
    print()
space = 1
for i in range(1, halfdiamondrow):
    for j in range(1, space + 1):
        print(end=' ')
    space += 1
    num = 1
    for j in range(1, 2 * (halfdiamondrow - i)):
        print(end=str(num))
        num += 1
    print()