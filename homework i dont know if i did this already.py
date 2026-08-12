books = ['harry potter', 'charlie and chocolate factory', 'matida', 'voyagers series', 'wonder']
copy_counts = [9, 3, 0, 14, 7]

library = {book: count for book, count in zip(books, copy_counts)}
print('Full library sotck is', library)

available_books = [book for book in books if library[book] > 0]
print('\nThe books available are', available_books)

chosen_book = input('Which book do you want to borrow')

if chosen_book not in library or library[chosen_book] == 0:
    print(chosen_book, 'is not in the library or is already checked out to someone \n stopping the checker')

late_fees = [5,8,4,6,7]
extra_fee = int(input('Enter one of the late book fees '))

updated_fees = list(map(lambda fee: fee + extra_fee, late_fees))
print('Updated late fees', updated_fees)

book_index = books.index(chosen_book)
chosen_fee = updated_fees[book_index]
print('The late fee for', chosen_book,'is', chosen_fee)

library[chosen_book] = library[chosen_book] - 1
print('You have borrowed',chosen_book,'these are the remaining amounts', library[chosen_book])

print("")
print("===== LIBRARY BOOK AVAILABILITY CHECKER =====")
print("Book Borrowed:", chosen_book)
print("Late Fee:", chosen_fee)
print("Updated Library Stock:", library)
print("=============================================")