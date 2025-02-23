owner_max = ''
pet_max = ''
longest_owner = 0
longest_pet = 0

owner_name = "Full name:"
owner_age = "Age:"
owner_sex = "Gender:"
owner_id = "ID:"
owner_address = "Address:"
owner_city = "City:"
owner_state = "State:"
owner_zip = "Zipcode:"
owner_cred_deb = "Credit/Debit number:"

pet_name = "Name:"
pet_age = "Age:"
animal_type = "Animal:"
animal_mood = "Behavior"
animal_check_up = "Last checkup date:"


owner_length = [
    "Full name:",
    "Age:",
    "Gender:",
    "ID:",
    "Address:",
    "City:",
    "State:",
    "Zipcode:",
    "Credit/Debit number:",
    ]

    
pet_length = [
    "Name:",
    "Age:",
    "Animal:",
    "Behavior",
    "Last checkup date:", 
    ]


owner_max = max(owner_length, key=len)
#print(owner_max)
longest_owner = (len(owner_max))
#print(longest_owner)

pet_max = max(pet_length, key=len)
#print(pet_max)
longest_pet = (len(pet_max))
#print(longest_pet)

def calculate_space(statement, max_length):
    
    current_length = 0
    length = len(statement)
    current_length = max_length - length
    space = " " * current_length + "\t\t"
    return space

""" 
new_space = calculate_space(owner_zip, longest_owner)
new_space_2 = calculate_space(owner_cred_deb, longest_owner)

print(f"{owner_cred_deb}" + f"{new_space_2}" + "238402384245")
print(f"{owner_zip}" + f"{new_space}" + "7745 florgon st ne")

 """

