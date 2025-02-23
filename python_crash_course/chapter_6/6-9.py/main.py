import sys
fav_place = {}

exit_program = True
name = ''
fav_restuarant = ''

print("\n")

while exit_program:
 
    response = input(f"Enter your name:\n")
    if response.lower() == "exit":
        sys.exit()
    else:
        name = response
    
      
    response = input(f"Enter your favorite restuarant:\n")
    if response.lower() == "exit":
        sys.exit()
    else:
        fav_restuarant = response
    
    fav_place[name] = fav_restuarant
    
    while True:
    
        response = input("Would you like to add another person to the list?\n")
        
        if response.lower() == "yes":
            break
        elif response.lower() == "no":
            exit_program = False
            break
        else:
            print("That is not a valid response. Please enter yes or no.\n")
        
    


for user, user_info in fav_place.items():
    print(f"{user.title()}'s favorite restuarant is {user_info.title()}.")

print("\n")