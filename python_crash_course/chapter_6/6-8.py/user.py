
current_id = []

# function to store information on the owner
def add_owner():
    
    license_id = 0
    first_name = ''
    last_name = ''
    address = ''
    city = ''
    state = ''
    zip_code = 0
    age = 0
    sex = ''
    credit_debit = 0
    
    owner_info = {
        'first name' : first_name,
        'last name' : last_name,
        'address' : address,
        'city' : city,
        'state' : state,
        'zip code' : zip_code,
        'age' : age,
        'sex' : sex,
        'credit/debit' : credit_debit,    
    }
    
    response = input(f"Enter your first name:\n")
    if response.lower == 'exit':
        return license_id, owner_info
    else:
        owner_info['first name'] = response
    
    response = input(f"Enter your last name:\n")
    if response.lower == 'exit':
        return license_id, owner_info
    else:
        owner_info['last name'] = response
    
    response = input(f"Enter your address:\n")
    if response.lower == 'exit':
        return license_id, owner_info
    else:
        owner_info['address'] = response
        
    response = input(f"Enter the city you live in:\n")
    if response.lower == 'exit':
        return license_id, owner_info
    else:
        owner_info['city'] = response
    
    response = input(f"Enter the state you live in:\n")
    if response.lower == 'exit':
        return license_id, owner_info
    else:
        owner_info['state'] = response
        
    response = input(f"Enter the zipcode for your city:\n")
    if response.lower == 'exit':
        return license_id, owner_info
    else:
        owner_info['zip code'] = response
    
    response = input(f"Enter your age:\n")
    if response.lower == 'exit':
        return license_id, owner_info
    else:
        owner_info['age'] = response
        
    response = input(f"Enter your gender:\n")
    if response.lower == 'exit':
        return license_id, owner_info
    else:
        owner_info['sex'] = response
    
    confirm = True
    
    while confirm:
        
        id_found = False
        
        response = input(f"Enter your ID:\n")
        
        if current_id:
            for id in current_id:
                if id == response:
                    id_found = True
                    
        if response.lower == 'exit':
            return license_id, owner_info
        
        if id_found == True:
            print("\nThis id is under someone else's name.\nPlease provide a valid id:\n")   
        else:
            license_id = response
            current_id.append(response)
            confirm = False
            
    response = input(f"Enter your credit or debit number:\n")
    if response.lower == 'exit':
        return license_id, owner_info
    else:
        owner_info['credit/debit'] = response
            
    return license_id, owner_info
        
        
# function to store information on the pet  
def add_pet():
    owner_id = current_id[-1]
    name = '' 
    age = 0
    animal_type = ''
    check_up_date = ''
    behavior_status = ''
    allergies = []

    animal_info = {
        'name' : name, 
        'age' : age,
        'animal type' : animal_type,
        'last checkup' : check_up_date, 
        'behavior' : behavior_status, 
        'allergies' : allergies, 
    }
    
    
    response = input("Enter the animal's name:\n")
    if response.lower() == 'exit':
        return owner_id, animal_info
    else:
        animal_info['name'] = response
    
    response = input("Enter the animal's age:\n")
    if response.lower() == 'exit':
        return owner_id, animal_info
    else:
        animal_info['age'] = response
        
    response = input("Enter the type of animal:\n")
    if response.lower() == 'exit':
        return owner_id, animal_info
    else:
        animal_info['animal type'] = response
    
    response = input("Enter the date of the animal's last check up:\n")
    if response.lower() == 'exit':
        return owner_id, animal_info
    else:
        animal_info['last checkup'] = response
        
    response = input("Enter the behavior of the animal:\n")
    if response.lower() == 'exit':
        return owner_id, animal_info
    else:
        animal_info['behavior'] = response
    
    print("Enter any allergies the animal has:")
    while True:
        response = input()
        if response.lower() == 'exit':
            break
        else:
            animal_info['allergies'].append(response)
    
    return owner_id, animal_info

    

        
    
    
    
    
    
    
    
    
    
    
    
    