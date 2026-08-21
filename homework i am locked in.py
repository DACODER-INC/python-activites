class pet:
    print('I am a pet profile keeper ran on classes in python')
 
pet_object = pet()

class petprofile:
    

    category = pet

    def __init__ (self, name, animal_type, age, favorite_food):
        

        self.name = name
        self.animal_type = animal_type
        self.age = age
        self.favorite_food = favorite_food

pet1 = petprofile('Bingo', 'Dog', 5, 'Dog Treats')
pet2 = petprofile('Rio', 'Parrot', 3, 'Almonds')


print('Meet',pet1.name,'he is a',pet1.animal_type,'he is', pet1.age,'years old and he loves',pet1.favorite_food)
print('and meet',pet2.name,'he is a',pet2.animal_type,'he is',pet2.age,'years old and he loves',pet2.favorite_food)