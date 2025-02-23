from random import randint

lottery_combo = (1, 2, 3, 4, 5, 6, 7, 8, 9, 'f', 'z', 'g', 'a', 'r')

winning_lotto = ''

my_lotto = "2z9a"

counter = 0

match = True

while match:

    for i in range(4):
        num = randint(1, len(lottery_combo))
        current_value = str(lottery_combo[num - 1])
        winning_lotto += current_value
    
    
    if my_lotto == winning_lotto:
        match = False
        
    counter += 1
    winning_lotto = ''
    
print(f"\nIt took {counter} tries to find the winning lottery ticket!\n")
