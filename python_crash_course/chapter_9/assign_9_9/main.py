from classes import *

my_tesla = ElectricCar('Roadster', '5', 2022)

divider = "_" * 60

print(f"{divider}\n")
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
print(f"{divider}\n")
