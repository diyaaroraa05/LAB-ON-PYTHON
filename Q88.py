# WAP to demonstrate class, object, properties and methods
class Car: 
    def __init__(self, make, model, year): 
        self.make = make
        self.model = model 
        self.year = year 
    def display_info(self): 
        print(f"{self.year} {self.make} {self.model}")
my_car = Car("Toyota", "Corolla", 2020) 
my_car.display_info()

print("This code is written by DIYA ARORA ERP-0221BCA059")
