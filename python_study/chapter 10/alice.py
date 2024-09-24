""" # Handling the FileNotFoundError Exception
""" filename = 'chapter 10/alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()

except FileNotFoundError:
    print(f'Sorry, the file "{filename}" does not exist.') 
 """
""" # assigning string to variable title
title = "Alice in Wonderland"
# using split message to seperate each word in title.
print(title.split()) 


filename = 'chapter 10/alice.txt'

with open(filename, 'w') as alice:
    alice_info = alice.write("Alice in Wonderland")


try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")


else:
    # Count the approximate nuber of words in the file .
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")


 
    