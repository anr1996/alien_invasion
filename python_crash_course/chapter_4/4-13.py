buffet_list = ('fried chicken', 'macaroni and cheese', 'sirloin steak', 'lobster', 'biscuits')

print("\n")
num = 0
for food in buffet_list:
    num += 1
    print(f"{num}.) {food.title()}")
num = 0
print("\n")

# buffet_list[0] = ('chicken fried steak') attempted to modify tuple to intentionally cause an error
# we are demonstrating here that tuples are immutable lists which cannot be altered.

buffet_list = ('chicken alfredo', 'cheeseburger', 'sirloin steak', 'lobster', 'biscuits')
for food in buffet_list:
    num += 1
    print(f"{num}.) {food.title()}")
num = 0
print("\n")

