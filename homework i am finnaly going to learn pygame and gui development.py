class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    
    def borrow(self):
        if self.is_borrowed:
            print(f'"{self.title}" has already been borrowed')
        else:
            self.is_borrowed = True
            print(f'"{self.title}"has been borrowed thank you')

    def return_book(self):
        if not self.is_borrowed:
            print(f'"{self.title}" has not been borrowed')
        else:
            self.is_borrowed = False
            print(f'"{self.title}"has been returned thank you')
    
    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f'{self.title} by {self.author} [{status}]'


book1 = Book('Project alpha', 'D.J Machalle')
book2 = Book('Matilda', 'Roald Dahl')
book3 = Book('The BFG', 'Roald Dahl')


print('=' * 42)
print('           LIBRARY SYSTEM')
print('=' * 42)
print(book1)
print(book2)
print(book3)
print()

book1.borrow()
book2.borrow()
book1.borrow()
print()

book1.return_book()
book3.return_book()
print()

print(book1)
print(book2)
print(book3)
            

