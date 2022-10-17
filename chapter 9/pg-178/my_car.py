""" 
# importing Car module from car.py
from car import Car

importing ElectricCar module from electric_car.py
from electric_car import ElectricCar

my_beetle = Car('Volkswagon', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

 """

""" # Usings Aliases

# importing Car module using alias C
from car import Car as C

# importing ElectricCar module using alias EC
from electric_car import ElectricCar as EC

my_honda = C('honda', 'civic', 2020)
print(my_honda.get_descriptive_name())

my_tesla = EC('tesla', 'model s', 2022)
print(my_tesla.get_descriptive_name())
 """
