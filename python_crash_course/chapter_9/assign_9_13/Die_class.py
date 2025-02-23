from random import randint

class Die:
    def __init__(self):
        self.sides = 6
        
    def roll_die(self):
        num = randint(1, self.sides)
        
        print(num)
    
    def set_sides(self,num_sides):
        self.sides = num_sides
        

    
    