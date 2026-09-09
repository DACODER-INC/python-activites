class Book:
    is_borrowed = False
    def __init__(self, title, author):
        self.title = title
        self.author = author
        

    def borrow(self, title, author):
        print('Thank you for borrowing', self.title,'by', self.author)
        is_borrowed = True



    def return_book(self):
        print('Thank you for giving it back')
        is_borrowed = False


obj = Book('Matilda', 'Roald Dahl')
obj1 = Book('Harry potter', 'Jk rowling')
obj2 = Book('Project alpha', 'D J machalle')
obj.borrow('Matilda', 'Roald Dahl')
obj.return_book()
obj1.borrow('Harry potter','Jk rowling' )
obj1.return_book()
obj2.borrow('Project alpha', 'D J machalle')
obj2.return_book()


