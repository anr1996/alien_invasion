# conditional tests

color_list = ['red', 'yellow', 'blue', 'green']
print("\nI am going to guess whether a certain color is present in a box of colors.\n")

guess_color = 'blue violet'
print(f"\nI predict that the color {guess_color} is in the color box.")

color_found = False

for color in color_list:
    if color == guess_color:
        color_found = True
        break
    color_found = False

if color_found == False:
    print(f"{color_found}! Guess again.\n")
else:
    print(f"{color_found}! good guess!\n")
    
    
guess_color = 'green'
print(f"\nI predict that the color {guess_color} is in the color box.")

for color in color_list:
    if color == guess_color:
        color_found = True
        break
    color_found = False

if color_found == False:
    print(f"{color_found}! Guess again.\n")
else:
    print(f"{color_found}! good guess!\n")

guess_color = 'red'
print(f"\nI predict that the color {guess_color} is in the color box.")

for color in color_list:
    if color == guess_color:
        color_found = True
        break
    color_found = False

if color_found == False:
    print(f"{color_found}! Guess again.\n")
else:
    print(f"{color_found}! good guess!\n")
    
guess_color = 'scarlet'
print(f"\nI predict that the color {guess_color} is in the color box.")

for color in color_list:
    if color == guess_color:
        color_found = True
        break
    color_found = False

if color_found == False:
    print(f"{color_found}! Guess again.\n")
else:
    print(f"{color_found}! good guess!\n")




    



    
