# storing data 
# Using json.dump() and json.load()

# import json module
import json

# creating list of numbers
numbers = [2, 3, 5, 7, 11, 13]

# choosing file name to store list of numbers
filename = 'numbers.json'

# opening file in write code.
with open(filename, 'w') as f:

    # storing list of numbers in file numbers.json
    json.dump(numbers, f)
