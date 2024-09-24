""" # Large Files: One Million Digits
filename = 'chapter 10/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

# print the first 52 digits of the file 'pi_million_digits.txt'
print(f"{pi_string[:52]}")
 """




""" filename = 'chapter 10/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first milion digits of pi!")
else: 
    print("Your birthday does not appear in the first million digits of pi. ")


 """