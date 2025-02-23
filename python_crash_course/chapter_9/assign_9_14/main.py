from random import randint

lottery_combo = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'f', 'z', 'g', 'a', 'r')

winning_lotto = ''

for i in range(4):
    num = randint(1, len(lottery_combo))
    current_value = str(lottery_combo[num - 1])
    winning_lotto += current_value + " "

print("\nThe winning lottery ticket is:")
print(f"{winning_lotto}\n")

