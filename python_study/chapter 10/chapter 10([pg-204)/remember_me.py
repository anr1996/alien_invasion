""" # Saving and Reading User-Generated Data

# import module json
import json

# asking for user input
username = input("What is your name? ")


filename = 'username.json'

with open(filename, 'w') as f:
    
    # passing username and file object to json.dump to store username in a file.
    json.dump(username, f)

    # printing message informing user that we have stored their information.
    print(f"We'll remember you when you come back, {username}!")


 """
""" 

import json

# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
filename = 'username.json'




try:

    # opening file username.json 
    # if file exists, read it back into memory
    with open(filename) as f:
        username = json.load(f)

    # if file doesn't exist run except block 'FileNotFoundError'
except FileNotFoundError:
    username = input("What is your name? ")

    # opening file username.json
    with open(filename, 'w') as f:
        
        # storing name from file username.json in username.
        json.dump(username, f)

        # print message with username .
        print(f"we'll remember you when you come back, {username}!")

else:
    # welcome back the user.
    print(f"Welcome back, {username}!")
 """


# Refactoring

""" import json

def greet_user():
    """"Greet the user by name.""""
    filename = 'username.json'

    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What  is your name? ")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"we'll remember you when you come back, {username}!")
    else:
        print(f"Welcome back, {username}!")
greet_user()
 """

""" 
import json

def get_stored_username():
    """"Get stored username if available.""""
    filename = 'username14.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

get_stored_username()

def greet_user():
    """"Greet the user by name.""""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        filename = 'username14.json'
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}! ")

greet_user()
 """

import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'usernamee.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username




def get_new_username():
    """Prompt for a new usename."""
    username = input("What is your name? ")
    filename = 'usernamee.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}! ")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}! ")
greet_user()

