import json

filename = 'num.json'

with open (filename) as f:
    number = json.load(f)
    print(f"Your favorite number is {number}")