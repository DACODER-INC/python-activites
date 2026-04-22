numofrows = int(input("Enter the number of rows for the floyds triangle: "))
num = 1
for i in range(1, numofrows + 1):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()