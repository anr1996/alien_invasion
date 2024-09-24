""" 
with open('guest_book', 'w') as guest_info:
    contents = guest_info.write(f"hi\n")


with open('guest_book', 'a') as guest_info:
    contents = guest_info.write(f"high\n") """

""" 
user = input("What is your name? : ")
print(f"welcome {user}")

filename = 'chapter 10/guest_book.txt'
with open(filename, 'w') as guest_book:
    guest_book.write("")


active = True
while active:
    with open(filename, 'a') as guest_info:
        guest_info.write(f"{user}\n")
 """
    

""" filename = 'chapter 10/guest_book.text'

with open(filename, 'w') as guest_book:
    guest_book.write("")

with open(filename, 'a') as guest_book:
    guest_book.write(f"hi\n")
     
with open(filename, 'a') as guest_book:
    guest_book.write(f"adrian\n")
 """



filename = 'chapter 10/guest_book.text'

# creating empty file
with open(filename, 'w') as guest_book:
    guest_book.write("")

# creating flag and setting it to true
active = True
while active:
    
    # asking for input
    message = input("whats your name? : ")

    if message == 'quit':
        active = False
    else:
        
        # appending to file 'filename'
        with open(filename, 'a') as guest_update:
            guest_update.write(f"{message}\n")
            print(f"welcome {message}.")
        





  