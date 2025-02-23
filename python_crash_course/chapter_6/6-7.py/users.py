
def add_user():
    
    username = ''
    first_name = ''
    last_name = ''
    social_sec = 0
    address = 0
    city = ''
    state = ''
    zip_code = 0
    age = 0
    sex = ''
    
    user_info = {
        'first name' : first_name,
        'last name' : last_name,
        'social security' : social_sec,
        'address' : address,
        'city' : city,
        'state' : state,
        'zipcode' : zip_code,
        'age' : age,
        'sex' : sex,
    }
    
    response = input(f"\nEnter a username:\n")
    
    if response.lower() == 'exit':
        return username, user_info
    else:
        username = response
        
    response = input(f"\nEnter your first name:\n")
    
    if response.lower() == 'exit':
        return username, user_info
    else:
        user_info['first name'] = response
    
    response = input(f"\nEnter your last name:\n")
    
    if response.lower() == 'exit':
        return username, user_info
    else:
        user_info['last name'] = response
    
    response = input(f"\nEnter your social security number:\n")
    
    if response.lower() == 'exit':
        return username, user_info
    else:
        user_info['social security'] = response
    
         
    response = input(f"\nEnter your address:\n")
    
    if response.lower() == 'exit':
        return username, user_info
    else:
        user_info['address'] = response
    
    response = input(f"\nEnter the city you live in:\n")
    
    if response.lower() == 'exit':
        return username, user_info
    else:
        user_info['city'] = response
    
    response = input(f"\nEnter the state you live in:\n")
    
    if response.lower() == 'exit':
        return username, user_info
    else:
        user_info['state'] = response
    
         
    response = input(f"\nEnter your zipcode:\n")
    
    if response.lower() == 'exit':
        return username, user_info
    else:
        user_info['zipcode'] = response
    
    response = input(f"\nEnter your age:\n")
    
    if response.lower() == 'exit':
        return username, user_info
    else:
        user_info['age'] = response
    
    response = input(f"\nEnter your gender:\n")
    
    if response.lower() == 'exit':
        return username, user_info
    else:
        user_info['sex'] = response
    
    return username, user_info
    
    
    
        
        
        
        
    
    
        

        
    