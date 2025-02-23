import json

num = int(input("What is your favorite number?\n"))

filename = 'num.json'

with open(filename, 'w') as f:
    json.dump(num, f)
    
