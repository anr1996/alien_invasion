import json
import os



def get_stored_num():
    filename = 'num.json'
    
    try:

        with open (filename) as f:
            number = json.load(f)
    
    except FileNotFoundError:
        return None
    else:
        return number


def get_new_num():
    num = int(input("What is your favorite number?\n"))
    filename = 'num.json'
    with open(filename, 'w') as f:
        json.dump(num, f)
    
    return num

        
def greet_user():
    num = get_stored_num()
    
    if num:
        print(f"Your favorite number is {num}\n")
    else:
        num = get_new_num()
        print(f"Your favorite number is {num}")
        
        
def create_user():
    user = input("Enter a desired username: ")
    
    filename = 'user.json'
    with open(filename, 'w') as f:
        json.dump(user, f)
    
    print(f"Welcome {user}")



        
def verify_user():

    filename = 'user.json'
    filename_2 = 'num.json'
    
    try:

        with open (filename) as f:
            user = json.load(f)
    
    except FileNotFoundError:
        print("You are the first visitor! Please create a username.\n")
        create_user()
        
        if os.path.exists(filename_2):
            os.remove(filename_2)
        
    
    else:
       user_response = input(f"Is {user} the right user name?\n")
       if user_response == 'yes'.lower():
           print(f"Welcome back {user}!")
       else:
            create_user()
            if os.path.exists(filename_2):
                os.remove(filename_2)
        
           
   
    
    
       
    
    
    