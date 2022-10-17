# Programming Poll
active = True

user_poll = 'chapter 10/programming_poll.txt'
with open(user_poll, 'w') as user_info:
    user_info.write("")

while active:
    message = input("what is your name? : ")
    

    if message == 'quit':
        active = False

    else:
        
        print(f"hello {message}.")
        with open(user_poll, 'a') as save_name:
            save_name.write(f"{message}:\t")
        response = input("what do you like about programming? : ")
        with open(user_poll, 'a') as user_update:
            user_update.write(f"{response}\n") 
