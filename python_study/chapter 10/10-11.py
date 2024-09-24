
import json

response = input("What is your favorite number?: ")
filename = 'favorite_number.json'

with open(filename, 'w') as f:
    json.dump(response, f)



with open(filename, 'r') as read:
    contents = read.read()

print(f"I now know that your favorite number is {contents}")






