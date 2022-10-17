""" # importing multiple classes Car, ElectricCar from module car.py
from car import Car, ElectricCar

# assigning variables to class Car
my_beetle = Car('volkswagen', 'beetle', 2019)

# calling instance
print(my_beetle.get_descriptive_name())

# assigning variables to class ElectricCar
my_tesla_2 = ElectricCar('tesla', 'roadster', 2019)

# calling instance
print(my_tesla_2.get_descriptive_name()) """



# Importing an Entire Module

# importing entire module car.py
"""
import car

my_beetle = car.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2020)
print(my_tesla.get_descriptive_name())
 """

# Importing a Module into a Module


