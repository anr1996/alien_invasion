# try except block
try:

    rat = 'rat.txt'
    with open(rat) as dirty_rodent:
        for line in dirty_rodent:
            print(f"{line}\n")

except FileNotFoundError:
    # passing error silently
    pass



kitten = 'silent_kitten.txt'

with open('silent_kitten.txt', 'w') as cat_stuff:
    cat_stuff.write('fucking cats!')
    
with open(kitten) as file_object:
    for line in file_object:
        print(f"{line}\n")

dog = 'silent_dog.txt'
        
with open(dog, 'w') as dog_list:
    dog_list.write('dogs are hyper!\n')

with open(dog, 'a') as dog_lists:
    dog_lists.write('dogs are loyal too! and not so evil\n')

with open(dog, 'a') as dog_lists:
    dog_lists.write('dogs are messy, oh well\n')

with open(dog) as dog_quotes:
    for line in dog_quotes:
        print(f"{line}\n")

