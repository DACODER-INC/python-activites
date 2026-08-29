class Vehicle:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed
    

    def show_details(self):
        print(self.brand,'is the brand')
        print('The max speed is', self.max_speed,'KM/H')

class Car(Vehicle):
    def __init__(self, model, seats, brand, max_speed):
        self.model = model
        self.seats = seats
        super().__init__(brand, max_speed)
    
    def show_details(self):
        print('The model is', self.model)
        print('The seats are',self.seats)
        super().show_details()
    
    def fuel_type(self, fuel):
        print(self.model, 'uses', fuel)


The_car = Car('Model Y Premium awd', 7, 'Tesla', 201)
The_car.show_details()
The_car.fuel_type('Electric')

print('Is car a sub class of vehicle', issubclass(Car, Vehicle))