# importing module car into module electric_car

from car import Car

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
   