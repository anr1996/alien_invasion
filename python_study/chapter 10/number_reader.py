# importing module json
import json

# assigning variable 'filename' to 'numbers.json'.
filename = 'numbers.json'

# opening file
with open (filename) as f:

    # loading file
    numbers = json.load(f)

# printing contents of file to terminal
print(numbers)

