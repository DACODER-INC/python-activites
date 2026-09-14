class Account:
    def __init__(self, owner, pin):
        self.owner = owner
        self.__pin = pin

    def show_pin_status(self):
        print('Account holder is:', self.owner)    
        print('The pin is safely secured')
    
    def set_pin(self, new_pin):
       if len(new_pin) == 4 and new_pin.isdigit():
         self.__pin = new_pin
         print('PIN updated successfully.')
       else:
        print('Invalid PIN. PIN must be exactly 4 digits.')

    

    def check_pin(self, entered_pin):
        if entered_pin == self.__pin:
            print('Access Granted')
        else:
            print('Access Denied')
    

    def __str__(self):
        return 'Account holder:' + self.owner


my_account = Account('Navraj', '0508')
print(my_account)


my_account.show_pin_status()


my_account.__pin = '9999'
print('Tried changing the pin from outside')


my_account.check_pin('9999')
my_account.check_pin('0508')


my_account.set_pin('9999')

my_account.check_pin('9999')