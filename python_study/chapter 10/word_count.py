
""" with open('alice_2.txt', 'w') as new_file_1:
    new_file_1.write("")

with open('moby_dick.txt', 'w') as new_file_2:
    new_file_2.write("")

with open('little_women.txt', 'w') as new_file_3:
    new_file_3.write("")
 """


""" 
def count_words(filename):
    """"Count the approximate number of words in a file.""""

    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['alice_2.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename) """



def count_words(filename):
    """Count the approximate number of words in a file."""

    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # failing code silently
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['alice_2.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
 