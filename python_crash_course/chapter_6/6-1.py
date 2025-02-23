# Person

users = {}

def add_user():
    id_num = ''
    first_name = ''
    last_name = ''
    age = ''
    city = ''
    zipcode = '' 
    
    user_info = {
        'First name' : first_name,
        'Last name' : last_name,
        'Age' : age,
        'City' : city,
        'Zipcode' : zipcode,
    }
    
    response = input("\nEnter your identification number:\n\n") 
    
    if response.lower() == 'exit':
        return id_num, user_info
    
    else:
        id_num = response
    
    response = input("Enter your first name:\n") 
    
    if response.lower() == 'exit':
        return id_num, user_info
    else:
        user_info['First name'] = response
    
    response = input("Enter your last name:\n") 
    
    if response.lower() == 'exit':
        return id_num, user_info
    else:
        user_info['Last name'] = response
        
    response = input("Enter your age:\n") 
    
    if response.lower() == 'exit':
        return id_num, user_info
    else:
        user_info['Age'] = response
        
    response = input("Enter the city you currently live in:\n") 
    
    if response.lower() == 'exit':
        return id_num, user_info
    else:
        user_info['City'] = response
    
    response = input("Enter the zipcode for the city you live in:\n") 
    
    if response.lower() == 'exit':
        return id_num, user_info
    else:
        user_info['Zipcode'] = response
        
    return id_num, user_info


print("Type exit at any time to leave the user profile creation menu\n")

while True:
    
    id_num, user_data = add_user()
    users[id_num] = user_data
    response = input("\nWould you like to enter another user?\n\n")
    if response.lower() == 'no':
        break

for id_num, user_data in users.items():
    print("\n")
    print(f"User Id: {id_num}")
    print(f"First name: {user_data['First name'].title()}")
    print(f"Last name: {user_data['Last name'].title()}")
    print(f"Age: {user_data['Age']}")
    print(f"City: {user_data['City'].title()}")
    print(f"Zipcode: {user_data['Zipcode']}")

print("\n")
    
    
   


 

    
    
    
    

    
    



