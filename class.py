class Vehicle:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.mileage = 0

    def drive(self, miles):
        self.mileage += miles
        print(f"The {self.year} {self.brand} {self.model} has been driven for {miles} miles.")

    def describe_vehicle(self):
        print(f"This vehicle is a {self.year} {self.color} {self.brand} {self.model} with {self.mileage} miles.")

class ElectricVehicle(Vehicle):
    def __init__(self, brand, model, year, color, battery_capacity):
        super().__init__(brand, model, year, color)
        self.battery_capacity = battery_capacity
        self.charge_level = 100

    def charge(self):
        self.charge_level = 100
        print("The vehicle has been fully charged.")

    def describe_vehicle(self):
        super().describe_vehicle()
        print(f"It has a {self.battery_capacity} kWh battery with {self.charge_level}% charge.")

my_car = Vehicle("Toyota", "Corolla", 2015, "Silver")
my_car.drive(100)
my_car.describe_vehicle()

my_ev = ElectricVehicle("Tesla", "Model S", 2020, "Red", 100)
my_ev.drive(50)
my_ev.describe_vehicle()
my_ev.charge()
my_ev.describe_vehicle()







#Previous  Code
class Vehicle:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.mileage = 0

    def drive(self, miles):
        self.mileage += miles
        print(f"The {self.year} {self.brand} {self.model} has been driven for {miles} miles.")

    def describe_vehicle(self):
        print(f"This vehicle is a {self.year} {self.color} {self.brand} {self.model} with {self.mileage} miles.")

class ElectricVehicle(Vehicle):
    def __init__(self, brand, model, year, color, battery_capacity):
        super().__init__(brand, model, year, color)
        self.battery_capacity = battery_capacity
        self.charge_level = 100

    def charge(self):
        self.charge_level = 100
        print("The vehicle has been fully charged.")

    def describe_vehicle(self):
        super().describe_vehicle()
        print(f"It has a {self.battery_capacity} kWh battery with {self.charge_level}% charge.")

my_car = Vehicle("Toyota", "Corolla", 2015, "Silver")
my_car.drive(100)
my_car.describe_vehicle()

my_ev = ElectricVehicle("Tesla", "Model S", 2020, "Red", 100)
my_ev.drive(50)
my_ev.describe_vehicle()
my_ev.charge()
my_ev.describe_vehicle()

# Polymorphism Challenge
print("\nPolymorphism Challenge:")

class VehicleMove:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        pass

class Car(VehicleMove):
    def move(self):
        print(f"The {self.brand} {self.model} car is driving.")

class Plane(VehicleMove):
    def move(self):
        print(f"The {self.brand} {self.model} plane is flying.")

class Boat(VehicleMove):
    def move(self):
        print(f"The {self.brand} {self.model} boat is sailing.")

def make_vehicle_move(vehicle):
    vehicle.move()

car = Car("Toyota", "Corolla")
plane = Plane("Boeing", "747")
boat = Boat("Sailfish", "SF-1000")

make_vehicle_move(car)
make_vehicle_move(plane)
make_vehicle_move(boat)