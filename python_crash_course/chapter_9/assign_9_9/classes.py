
class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odemeter(self):
        print(f"This car has {self.read_odemeter_reading} miles on it.")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
    
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        self.odometer_reading += miles
    
class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size = 75):
        """Initialize the battery's attributes."""

        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery")
    
    def get_range(self):
        print(f"The range of the battery is {self.battery_size} miles on a full charge.")
    
    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100
        
        
        


class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
        