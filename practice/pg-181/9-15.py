# Lottery Analysis

# setting variable equal to 0
count = 0

# from random libary importing function choice.
from random import choice

# creating list with various integers
lottery = [1,2,3,4,5,6,7,8,9,13]

# applying flow control
# setting active to True so while loop will continue running
active = True

while active:

    # for loop
    for ticket in lottery:
        winner = choice(lottery)
        count = count +1
        if winner == 13:
            active = False
            print("winner!")
            print(f"The winning number was {winner}.")
            print(f"The number generator ran {count} times before reaching the number {winner}.")
            


""" count = 0

trash = ['john', 'jessse', 'james']

for stuff in trash:
    count = count+1

print(count) """


""" print(choice(my_ticket)) """