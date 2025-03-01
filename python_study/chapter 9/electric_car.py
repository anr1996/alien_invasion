
""" class Car:
    """"A simple attempt to represent a car.""""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage

        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    """"Represent aspects of a car, specific to electric vehicles.""""
    def __init__(self, make, model, year):
        """"Initizalize attributes of the parent class.""""
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name()) """


# Defining Attributes and Methods for the Child Class

""" class Car:
    """"A simple attempt to represent a car.""""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank_gallons = 10

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage

        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        self.odometer_reading += miles
    
    def fill_gas_tank(self):
        """"filling gas tank""""
        print(f"The gas tank is at {self.gas_tank_gallons} gallons.")

my_car = Car('honda', 'civic', 1996)
print(my_car.get_descriptive_name())
my_car.fill_gas_tank()
print(f"\n")
print(f"\n")
print(f"\n")

 # Overriding Methods from the Parent Class.
class ElectricCar(Car):
    """"Represent aspects of a car, specific to electric vehicles.""""
    def __init__(self, make, model, year):

        """"Initizalize attributes of the parent class.""""
        super().__init__(make, model, year)
        self.battery_size = 75
    
    def describe_battery(self):
        """"Print a statement describing the battery size.""""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """"Electric cars don't have gas tanks.""""
        print("This car doesn't need a gas tank dummy!")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.fill_gas_tank()
my_tesla.describe_battery() 
 """





class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 5
        self.gas_tank_gallons = 10

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage

        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        self.odometer_reading += miles
    
    def fill_gas_tank(self):
        """filling gas tank"""
        print(f"The gas tank is at {self.gas_tank_gallons} gallons.")



# Instances as Attributes

# defining class Battery for information on the cars battery.
class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_upgrade, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
        self.battery_upgrade = battery_upgrade
    


    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge. ")
    
        # when the battery equals 75 add 25, therefore the battery will now equal 100
    def battery_upgrades(self, battery_upgrade):
        self.battery_size += battery_upgrade
        
    
        


class ElectricCar(Car):
    
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year, ):
        """Initialize attributes of the parent class."""
        
        
        # calling method ElectricCar from parent class Car.
        super().__init__(make, model, year)
        self.battery = Battery(75)
        
    
    # defining function read_odometer from parent class Car
    def read_odometer(self):

        # returning attribute 'read_odometer' from parent class 'Car' using Super Method.
        return super().read_odometer()
   
   

my_tesla = ElectricCar('tesla', 'model s', 2019)

# define details for tesla car
print(my_tesla.get_descriptive_name())

# describe details for battery
my_tesla.battery.describe_battery()

# describe updated range of battery
my_tesla.battery.get_range()
print("\n")
print("Update based off new battery power:")

# increase battery by 25
my_tesla.battery.battery_upgrades(25)

# describe updated battery
my_tesla.battery.describe_battery()

# describe odometer reading
my_tesla.read_odometer()

# describe updated range of battery
my_tesla.battery.get_range()






 

