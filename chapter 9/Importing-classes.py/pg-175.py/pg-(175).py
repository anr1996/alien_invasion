# Storing Multiple Classes in Module.

# importing class ElectricCar from file car.py
from car import ElectricCar

# defining values for attributes in Electric_Car
my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
