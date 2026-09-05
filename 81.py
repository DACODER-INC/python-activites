from abc import ABC , abstractmethod
class animal(ABC):
    def move_here(self):
        pass

class human(animal):
    def move(self):
        print('I can work and run')





class snake(animal):
    def move(self):
        print('I can bite and kill')





class wolf(animal):
    def move(self):
        print('I can howl and move in packs')






class lion(animal):
    def move(self):
        print('I can roar and I am the king')
        

obj = human()
obj1 = snake()
obj2 = wolf()
obj3 = lion()
obj.move()
obj1.move()
obj2.move()
obj3.move()