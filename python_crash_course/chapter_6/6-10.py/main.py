

import sys

user_fav_num = {}
exit_program = True

while exit_program:
    
    name = ''
    fav_num = []
    
    response = input("Enter your name:\n")
    if response.lower() == 'exit':
        sys.exit()
    else:
        name = response
    
    exit_program_2 = True

    while exit_program_2:
   
        is_found = False
        
        response = input("Enter your favorite number(s):\n")
        
        if response.lower() == 'done':
            exit_program_2 = False
            break
        elif response.lower() == 'exit':
            sys.exit()
        else:
            if not fav_num:
                fav_num.append(response)
            else:
                for num in fav_num:
                    if response == num:
                        is_found = True
                        break
                
                if is_found == False:
                    fav_num.append(response)

    user_fav_num[name] = fav_num

    while True:
        
        response = input("Would you like to add another person? (yes/no):\n")
        if response.lower() == 'yes':
            break
        elif response.lower() == 'no':
            exit_program = False
            break
        else:
            print("That is not a valid response. Please enter yes or no.\n")
        
        
for user, user_info in user_fav_num.items():
    print(f"{user.title()}'s favorite numbers are:")
    for num in user_info:
        print(num)
    print("\n")
        


    