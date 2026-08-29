class myclass:
    __privvar = 2394857
    def __privmethod(self):
        print('I am inside a private method of class myclass and SOMEBODY GET ME OUT OF HERE')

    def hello(self):
        print('Private variable value ', myclass.__privvar)


obj = myclass()
obj.hello()
obj.__privmethod()