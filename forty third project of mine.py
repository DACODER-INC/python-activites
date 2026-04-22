numofrows = int(input("Enter the number of rows for the floyds triangle: "))
num = 1
for i in range(numofrows):
    for j in range(i + 1):
        print(num, end=" ")
        num += 1
    print()