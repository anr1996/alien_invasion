# verify User.


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
    username = input("What is your user name? ")
    filename = 'usernamee.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"{username} ")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}! ")


print("Is this your username?\n ")
greet_user()
print("\n")
response = input("yes / no: ")

if response == 'no':
    get_new_username()

elif response == 'yes':
    print(f"\nWelcome back:\n ")
    greet_user()
    print("\n")