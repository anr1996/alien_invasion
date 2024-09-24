


# 10-3

# assigning variable user to input function.
user = input("what is your name? : ")

# opening file and writing user input to file .
with open('chapter 10/guest_list.txt', 'w') as user_guest:
    user_guest.write(user) 
