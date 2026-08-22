class io_string:
    def __init__(self):
        self.str1 = ''
    def get_string(self):
        self.str1 = input('Enter a string: ')
    def print_string(self):
        print('The result is', self.str1.upper())


object = io_string()
object.get_string()
object.print_string()
