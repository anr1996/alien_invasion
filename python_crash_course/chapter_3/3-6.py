# More Guests:

guest_list = ['Albert Einstein', 'Richard Feynman', 'Martin Luther King Jr']

print(f"\n{guest_list[0]}, I would like to invite you to my dinner party.")
print(f"{guest_list[1]}, I would like to invite you to my dinner party.")
print(f"{guest_list[2]}, I would like to invite you to my dinner party.")

guest_cancel = guest_list.pop(0)

print(f"\n{guest_cancel} cannot make it to the Dinner party.")

guest_list.insert(0,'John F Kennedy')

print(f"\n{guest_list[0]}, I would like to invite you to my dinner party.")
print(f"{guest_list[1]}, I would like to invite you to my dinner party.")
print(f"{guest_list[2]}, I would like to invite you to my dinner party.\n")

print("I have found a larger dinner table. Therefore, I will invite more guest.\n")

guest_list.insert(0, 'Dr Jack Kruze')
list_middle = int(len(guest_list) / 2)
guest_list.insert(list_middle, 'Niels Bohr')
guest_list.append('Robert Oppenheimer')

for guest in guest_list:
    print(f"{guest} I would like to invite you to my dinner party.\n")

