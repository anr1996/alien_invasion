# importing class Car from car.py file
from car import Car

# defining values for attributes from the class Car.
my_new_car = Car('audi', 'a4', 2019)

# calling instances
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()


