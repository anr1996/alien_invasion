# Checking Usernames

current_users = []

while True:
    response = input("\nEnter the users you would like to add to the website:\n\n")
    
    if response.lower() != 'exit':
        current_users.append(response)
    else:
        break
   


new_users = []

while True:
    response = input("\nEnter the new users you would like to add to the website:\n\n")
    
    if response.lower() != 'exit':
        new_users.append(response)
    else:
        break
   

for i in range(len(new_users)):
    user_check = new_users[i]
    user_found = False
    
    for user in current_users:
        if user.lower() == user_check.lower():
            user_found = True
            print(f"\nThe username {user_check.title()} is already taken.")
            break
    
    if user_found == False:
        current_users.append(user_check)
        print(f"\nThe username {user_check.title()} is available.")

