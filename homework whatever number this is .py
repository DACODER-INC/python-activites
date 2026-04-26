num_of_rows = int(input('Enter the number of rows for the triangle and the mirrored triangle:'))
for i in range(num_of_rows):
    for j in range(i + 1):
        print('*', end=' ')
    print()
for i in range(num_of_rows - 1 + i):
    for j in range(num_of_rows - i):
        print('*', end=' ')
    print()
