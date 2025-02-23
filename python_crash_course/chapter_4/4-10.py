# Slices

import math
# list of functions being used from chapter 3:
"""
print(list[0])
print(list[0].title())
print(list[-1])
list[0] = 'new item'
list.append('item_2')
list.insert(0, 'item_3')
del list[0]
list.pop(3)
list.remove('ducati')
too_expensive = 'bmw'
list.remove(too_expensive)
list.sort()
list.sort(reverse=True)
print(sorted(list))
list.reverse()
print(len(list))
"""

popular_cities = ['Paris, France', 'London, United Kingdom', 'New York City, USA', 'Tokyo, Japan', 'Barcelona, Spain',
                  'Rome, Italy', 'Bangkok, Thailand', 'Istanbul, Turkey', 'Dubai, United Arab Emirates', 'Amsterdam, Netherlands']

print("\n")
    
for i in range(len(popular_cities)):
    print(f"{i+1}.) {popular_cities[i].lower()}")


print("\n")

for i in range(len(popular_cities)):
    print(f"{i+1}.) {popular_cities[i].title()}")

first_city = popular_cities[0]
first_city_loc = popular_cities.index(first_city)
print(f"\n{first_city_loc + 1}.) {popular_cities[0]}")

last_city = popular_cities[-1]
last_city_loc = popular_cities.index(last_city)
print(f"{last_city_loc + 1}.) {popular_cities[-1]}\n")

popular_cities[5] = 'Lisbon, Portugal'
print(f"The 6th location in the list of popular cities has been changed to {popular_cities[5]}\n")

for i in range(len(popular_cities)):
    print(f"{i+1}.) {popular_cities[i].title()}")

city_found = False
city_name = 'Hanoi, Vietnam'

for i in range(len(popular_cities)):
    if popular_cities[i].lower() == city_name.lower():
        city_found = True
        break

if city_found == False:
    popular_cities.append(city_name)
    
print("\n")

for i in range(len(popular_cities)):
    print(f"{i+1}.) {popular_cities[i].title()}")
    
print("\n")

for i in range(len(popular_cities)):
    if city_name == popular_cities[i]:
        print(f"{city_name.title()}, has been added to our list of locations.")
        break

print("\n")
    

    
city_found = False
city_name = 'Paris, France'

for i in range(len(popular_cities)):
    if popular_cities[i].lower() == city_name.lower():
        city_found = True
        break

if city_found == False:
    popular_cities.append(city_name)
    

for i in range(len(popular_cities)):
    print(f"{i+1}.) {popular_cities[i].title()}")

print("\n")

city_name = 'Portland, USA'
city_found = False

print(f"The list currently has {(len(popular_cities))} locations.\n")

for i in range(len(popular_cities)):
    if popular_cities[i].lower() == city_name.lower():
        city_found = True
        break

if city_found == False:
    popular_cities.insert(4, city_name)
    print(f"{city_name}, has been added to our list.\n")
else:
    print(f"{city_name} is already in the list!\n")
    

for i in range(len(popular_cities)):
    print(f"{i+1}.) {popular_cities[i].title()}")

print("\n")

city_name = 'Portland, USA'
city_found = False

print(f"The list currently has {(len(popular_cities))} locations.\n")

for i in range(len(popular_cities)):
    if popular_cities[i].lower() == city_name.lower():
        city_found = True
        break

if city_found == False:
    popular_cities.insert(4, city_name)
    print(f"{city_name}, has been added to our list.\n")
else:
    print(f"{city_name} is already in the list!\n")

for i in range(len(popular_cities)):
    print(f"{i+1}.) {popular_cities[i].title()}")

print("\n")

city_name = 'Barcelona, Spain'
city_found = False
city_index = 0

for i in range(len(popular_cities)):
    if popular_cities[i].lower() == city_name.lower():
        city_found = True
        city_index = i
        break

if city_found == True:
    del popular_cities[city_index]
    print(f"Removing {city_name}, at {city_index + 1}.) from the list.\n")
else:
    print(f"{city_name}, was not found in our list, so there is nothing to delete.")

for i in range(len(popular_cities)):
    print(f"{i+1}.) {popular_cities[i].title()}")

print("\n")

city_name = 'Barcelona, Spain'
city_found = False
city_index = 0

for i in range(len(popular_cities)):
    if popular_cities[i].lower() == city_name.lower():
        city_found = True
        city_index = i
        break

if city_found == True:
    del popular_cities[city_index]
    print(f"Removing {city_name}, at {city_index + 1}.) from the list.\n")
else:
    print(f"{city_name}, was not found in our list, so there is nothing to delete.\n")

for i in range(len(popular_cities)):
    print(f"{i+1}.) {popular_cities[i].title()}")

print("\n")

city_name = 'Bangkok, Thailand'
removed_name = ''

for i in range(len(popular_cities)):
    if popular_cities[i].lower() == city_name.lower():
        print(f"{city_name}, found at index {i}, location {i + 1}.\n")
        break

removed_name = popular_cities.pop(6)

print(f"{removed_name}, was removed from the list.\n")

for i in range(len(popular_cities)):
    print(f"{i + 1}.) {popular_cities[i].title()}")

print("\n")

########

city_name = 'Dubai, United Arab Emirates'
city_found = False
city_index = 0

for i in range(len(popular_cities)):
    if popular_cities[i].lower() == city_name.lower():
        city_found = True
        city_index = i
        break

if city_found == True:
    popular_cities.remove(city_name)
    print(f"Removing {city_name}, at {city_index + 1}.) from the list.\n")
else:
    print(f"{city_name}, was not found in our list, so there is nothing to delete.\n")

for i in range(len(popular_cities)):
    print(f"{i+1}.) {popular_cities[i].title()}")

print("\n")

popular_cities.sort()

for i in range(len(popular_cities)):
    print(f"{i+1}.) {popular_cities[i].title()}")
    
print("\n")

popular_cities.sort(reverse=True)

for i in range(len(popular_cities)):
    print(f"{i+1}.) {popular_cities[i].title()}")
    
print("\n")

count = 0
print("Temporarily sorted list:\n")
for city in sorted(popular_cities):
    count += 1
    print(f"{count}.) {city}")
    
print("\n Original list:\n")

for i in range(len(popular_cities)):
    print(f"{i+1}.) {popular_cities[i].title()}")

print("\n")

print(f"Original list has been permenantly changed by reversing it's order:\n")

popular_cities.reverse()

for i in range(len(popular_cities)):
    print(f"{i+1}.) {popular_cities[i].title()}")
    
print("\n")

print(f"The new updated list now has {len(popular_cities)} locations.\n")

print(f"The first three locations in the list of locations are {popular_cities[:3]}\n")


middle_num = math.ceil((len(popular_cities)) / 2)

print(f"Three locations in the middle of the list are: {popular_cities[middle_num - 2:middle_num+1]}\n")

print(f"The last three locations in the list are: {popular_cities[-3:]}")





    
    

