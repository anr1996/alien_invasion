
exit = True
file_name = 'guest_book.txt'
while exit:
    name = input("Enter Your name:\n")
    if name.lower() == 'exit':
        exit = False
    else:
        with open(file_name, 'a') as file_object:
            file_object.write(name + "\n")
            print(f"Welcome {name}!\n")
        
    