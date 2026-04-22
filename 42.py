numofrows = int(input("Enter the number of rows: "))
for i in range(numofrows):
    for j in range(i + 1):
        print("*", end="")
    print()