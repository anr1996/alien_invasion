# Alien Colors #3

response = input("What color alien did you shoot?\n")
total_points = 0
alien_killed = ''

if response.lower() == 'green':
    alien_killed = response.lower() + ' alien'
    total_points += 5

elif response.lower() == 'yellow':
    alien_killed = response.lower() + ' alien'
    total_points += 10
    
elif response.lower() == 'red':
    alien_killed = response.lower() + ' alien'
    total_points += 15

else:
    alien_killed = 'nothing'

print(f"You killed {alien_killed}. Your total points are {total_points}.")



    

