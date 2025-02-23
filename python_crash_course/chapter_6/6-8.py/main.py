# Pets
from user import *
from statements import *

total_owners = {}
total_pets = {}




print("type 'exit' to exit the current menu at anytime")

divider = "\n" + ('-' * 70) + "\n"


confirm = True
while True:
    
    if confirm == False:
        break
    
    print(divider)
    
    owner_id, owner_info = add_owner()
    total_owners[owner_id] = owner_info
    
    print(divider)
    
    owner_id, pet_info = add_pet()
    total_pets[owner_id] = pet_info
    
    print(divider)
    

    
    while True:
        response = input(f"\nWould you like to add another customer and their pet: (yes/no)\n")
        if response.lower() == 'yes':
            break
        elif response.lower() == 'no':
            confirm = False
            break
        else:
            print(f"'{response}' is not a valid response. Please answer yes/no:\n")
          
print(divider)   

for id in current_id:
    
    print("(Owner)\n")
    length = calculate_space(owner_name, longest_owner)
    full_name = (f"{total_owners[id]['first name'].title()} " +
    f"{total_owners[id]['last name'].title()}")
    print("Full name:" + length + f"{full_name}\n")

    length = calculate_space(owner_age, longest_owner)
    print(f"Age:" + length +  f"{total_owners[id]['age']}\n")
    
    length = calculate_space(owner_sex, longest_owner)
    print(f"Gender:" + length + f"{total_owners[id]['sex']}\n")
    
    length = calculate_space(owner_id, longest_owner)
    print(f"ID:" + length + f"{id}\n")
    
    length = calculate_space(owner_address, longest_owner)
    print(f"Address:" + length + f"{total_owners[id]['address']}\n")
    
    length = calculate_space(owner_city, longest_owner)
    print(f"City:" + length + f"{total_owners[id]['city'].title()}\n")
    
    length = calculate_space(owner_state, longest_owner)
    print(f"State:" + length + f"{total_owners[id]['state'].title()}\n")
    
    length = calculate_space(owner_zip, longest_owner)
    print(f"Zipcode:" + length + f"{total_owners[id]['zip code']}\n")
    
    length = calculate_space(owner_cred_deb, longest_owner)
    print(f"Credit/Debit number:" + length + f"{total_owners[id]['credit/debit']}\n\n")
    

    
    print("\n\n(Pet)\n")
    
    length = calculate_space(pet_name,longest_pet)
    print(f"Name:" + length + f"{total_pets[id]['name'].title()}\n")
    
    length = calculate_space(pet_age,longest_pet)
    print(f"Age:" + length + f"{total_pets[id]['age']}\n")
    
    length = calculate_space(animal_type,longest_pet)
    print(f"Animal:" + length + f"{total_pets[id]['animal type'].title()}\n")

    print("Allergies: ")
    for allergy in total_pets[id]['allergies']:
        print(f"\n{allergy}")
    print("\n")
    
    
    length = calculate_space(animal_mood,longest_pet)
    print(f"Behavior:" + length + f"{total_pets[id]['behavior']}\n")
    
    length = calculate_space(animal_check_up,longest_pet)
    print(f"Last checkup date:" + length + f"{total_pets[id]['last checkup']}\n")
    print(divider)
    
  
    




 