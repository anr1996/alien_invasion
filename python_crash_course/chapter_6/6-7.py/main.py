# People
from users import *

total_users = {}

print("type 'exit' to leave the user creation menu at anytime")


divider = "\n" + ('-' * 60) + "\n"
print(divider)

while True:
    
    username, user_info = add_user()
    total_users[username] = user_info
    
    
    response = input(f"\nWould you like to add another user? yes/no:\n")
    
    if response.lower() == 'yes':
        
        continue
    elif response.lower() == 'no':
        break
    else:
        print(f" '{response}' is not a valid response. Please enter yes or no.\n")
    
print(divider)

for user, user_info in total_users.items():
    print("\nThe User's information is below:\n")
    print(f"\nUser: {user}\n")
    print(f"\nFull name: {user_info['first name'].title()} {user_info['last name'].title()}\n")
    print(f"\nSocial security number: {user_info['social security']}\n")
    print(f"\nLocation: " 
    + f"{user_info['address']}, "
    + f"{user_info['city']}, {user_info['state']}, {user_info['zipcode']}\n")
    print(f"\nAge: {user_info['age']}\n")
    print(f"\nGender: {user_info['sex']}\n")
    print(divider)
    



    