# My pizzas, Your pizzas

# Pizzas

my_fav_pizza = ['pepperoni', 'hawaiian', 'cheese']

print("\n")

for pizza in my_fav_pizza:
    print(f"{pizza.title()} pizza.")

print("\n")

for pizza in my_fav_pizza:
    print(f"I like {pizza.title()} pizza.")

print("\nPizza is awesome.\n")

friends_fav_pizza = []

friends_fav_pizza = my_fav_pizza[:]

my_fav_pizza.append('all meat')
friends_fav_pizza.append('veggie')

num = 0
print("My favorite pizzas are: ")
for pizza in my_fav_pizza:
    num += 1
    print(f"{num}.) {pizza}")
num = 0

print("\n")

num = 0
print("My friend's favorite pizzas are: ")
for pizza in friends_fav_pizza:
    num += 1
    print(f"{num}.) {pizza}")
num = 0

print("\n")

