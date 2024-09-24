# Dice

i = 10
from random import randint
random_numbers = randint
class die:
    def __init__(self, sides, die_2, die_3):
        self.sides = sides
        self.die_2 = die_2
        self.die_3 = die_3

    def random_num(self):
        print("printing random number between 1 and 6")
        print(random_numbers(1, self.sides)) 
        
    def random_num_2(self):
        print("printing random number between 1 and 10")
        print(random_numbers(1, self.die_2))

    def random_num_3(self):
        print("printing random number between 1 and 20")
        print(random_numbers(1, self.die_3))


# calling instance
roll = die(6, 10, 20)
roll.random_num()
print("\n")
roll.random_num_2()
print("\n")
roll.random_num_3()






        
    
