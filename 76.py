class FamilyMember:
    def __init__(self, eye_color, height_cm):
        self.eye_color = eye_color
        self.height_cm = height_cm
    def show_traits(self):
        print('eye color:', self.eye_color)
        print('Height in cm:', self.height_cm)
        
        
        
class Kid(FamilyMember):
    def __init__(self, name, age, eye_color, height_cm):
        self.name = name
        self.age = age
        FamilyMember.__init__(self, eye_color, height_cm)
    def show_traits(self):
        print('Name is ', self.name)
        print('age is:',self.age)
        super().show_traits()

    def fav_hobby(self, hobby):
        print(self.name, 'loves', hobby)


child = Kid('Navraj', 11, 'Dark brown', 160)
child.show_traits()
child.fav_hobby('technology')
print('is kid a sub class of family member?',issubclass(Kid, FamilyMember))
    