# hello admin

user_list = []

while True:
    response = input("\nEnter the users you would like to add to the website:\n\n")
    
    if response.lower() != 'exit':
        user_list.append(response)
    else:
        break
   


for user in user_list:
    if user.lower() == 'admin':
        print(f"\nHello {user}, would you like to see a status report?")
    else:
        print(f"\nWelcome {user}!")
        
        
if len(user_list) > 0:
    print(f"\nWe have {len(user_list)}.")
else:
    print("\nWe dont not have any users!")
    print("\nwe need to find users.")
    
user_list = []

if len(user_list) > 0:
    print(f"\nWe have {len(user_list)}.")
else:
    print("\nWe dont not have any users!")
    print("\nwe need to find users.")


