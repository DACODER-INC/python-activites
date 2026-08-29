class computer:
    def __init__(self):
            self.__maxprice = 90000000000000000000
    def sell(self):
        print('Selling price', self.__maxprice)
    def setmaxprice(self, price):
        self.__maxprice = price

obj = computer()
obj.sell()
obj.__maxprice = 1000
obj.sell()
obj.setmaxprice(90000)
obj.sell()