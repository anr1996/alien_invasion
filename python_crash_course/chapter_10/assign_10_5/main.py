
programming_poll = "/Users/adrianrich/Documents/python/python_crash_course/chapter_10/assign_10_5"\
    "/program_poll.txt"
    


while True:
    name = input("Enter Your name:\n")
    if name.lower() == 'exit':
        break
    
    fav = input("What is your favorite thing about programming?\n")
    if fav.lower() == 'exit':
        break
    
    with open(programming_poll, 'a') as file_object:
        file_object.write(name + ": " + fav + ".\n" )
    

            

        
    