# 10-11 Favorite Number

def stored_fav_num():
    filename = 'person_fav_num1.json'
    try:
        with open(filename) as f:
            favorite = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return favorite
        


import json
def new_fav_num():
    favorite_num = input("What is your favorite number: ")
    filename = 'person_fav_num1.json'
    with open(filename, 'w') as f:
        json.dump(favorite_num, f)
    return favorite_num


def greet_fav_num():
    favorite_numbers = stored_fav_num()
    if favorite_numbers:
        print(f"Your favorite number is {favorite_numbers}")
    else:
        favorite_numbers = new_fav_num()
        print(f"Now i know what your favorite number is !")

greet_fav_num()

