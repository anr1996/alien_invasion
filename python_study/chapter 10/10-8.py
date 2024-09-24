# Cats and Dogs

""" # setting variable equal to directory path for file pi_digits.txt
filename = 'chapter 10/pi_digits.txt'

# printing contents of file line by line
with open(filename) as file_object:
    for line in file_object:
        print(line) 
 """

""" filename = 'chapter 10/pi_digits.txt'
# opening file
with open(filename) as file_object:

    # setting variable equal to the contents of the file
    lines = file_object.readlines()

# Working with a files contents

for line in lines:
    print(line.rstrip()) """







try:

    rat = 'rat.txt'
    with open(rat) as dirty_rodent:
        for line in dirty_rodent:
            print(f"{line}\n")

except FileNotFoundError:
    print("File does not exist, are you looking in the right location? ")



kitten = 'kitten.txt'

with open('kitten.txt', 'w') as cat_stuff:
    cat_stuff.write('fucking cats!')
    
with open(kitten) as file_object:
    for line in file_object:
        print(f"{line}\n")

dog = 'dog.txt'
        
with open(dog, 'w') as dog_list:
    dog_list.write('dogs are hyper!\n')

with open(dog, 'a') as dog_lists:
    dog_lists.write('dogs are loyal too! and not so evil\n')

with open(dog, 'a') as dog_lists:
    dog_lists.write('dogs are messy, oh well\n')

with open(dog) as dog_quotes:
    for line in dog_quotes:
        print(f"{line}\n")





