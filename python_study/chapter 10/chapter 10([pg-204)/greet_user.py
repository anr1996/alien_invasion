# importing module json
import json


filename = 'username.json'

with open(filename) as f:

    # reading information stored in username.json and assigning it to the variable username.
    username = json.load(f)

    # printing message to user found in file username.json
    print(f"Welcome back, {username}!")


