
""" # opening file
with open('chapter 10/pi_digits.txt') as file_object:

    # read contents of file.
     contents = file_object.read()

# print contents of file to screen
print(contents)
 """

""" 
# opening file
with open('chapter 10/pi_digits.txt') as file_object:

    # read contents of file.
     contents = file_object.read()

# print contents of file to screen
# removing blank string at the end of the file using r strip method.
print(contents.rstrip()) """

""" 
# setting variable equal to directory path for file pi_digits.txt
filename = 'chapter 10/pi_digits.txt'

# printing contents of file line by line
with open(filename) as file_object:
    for line in file_object:
        print(line) """


""" filename = 'chapter 10/pi_digits.txt'
# opening file
with open(filename) as file_object:

    # setting variable equal to the contents of the file
    lines = file_object.readlines()

# Working with a files contents

for line in lines:
    print(line.rstrip()) """


""" filename = 'chapter 10/pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

# creating empty string to hold digits from file 'pi_digits.txt'
pi_string = ''

for line in lines:
    # placing contents of line in pi_string
    # removing white space
    pi_string += line.strip()

# printing new contents of pi_string
print(pi_string)

# printing number of objects in pi_string
print(len(pi_string))

 """





