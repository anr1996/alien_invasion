# Favorite numbers

users = {}

print("type exit to leave the questionaire anytime.")

def add_users():
    first_name = ''
    user_fav_num = ''
    
    fav_num = {
        'Favorite number' : user_fav_num,
    }
    
    response = input("\nWhat is your first name?\n")
    
    if response.lower() == 'exit':
        return first_name, fav_num
    else:
        first_name = response
        
    response = input("what is your favorite number?\n")
    
    if response.lower() == 'exit':
        return first_name, fav_num
    else:
        fav_num['Favorite number'] = response
    
    return first_name, fav_num
    

while True:
    first_name, fav_num = add_users()
    users[first_name] = fav_num
    response = input("\nWould you like to add another person's info?\n")
    if response.lower() == 'no':
        print("\n")
        break
    
for user, fav_num in users.items():
    print(f"Name: {user.title()}")
    print(f"Favorite number: {fav_num['Favorite number']}\n")
    
   
