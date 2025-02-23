# Dinner Guests:

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

print("""Sorry everyone The new dinner table will not arrive in time.\n
I will only be able to invite two guests.\n
I will notify everyone shortly about whether or not you are still invited to the dinner party.\n""")



while len(guest_list) > 2:
    
    guest_removed = guest_list.pop(len(guest_list)-1)
    print(f"{guest_removed} You are no longer invited to the dinner party. Sorry.\n")

print(guest_list)

for guest in guest_list:
    print(f"\n{guest} you are still invited to the dinner party!")

print(f"\nI will be inviting {len(guest_list)} guest to Dinner.")

while len(guest_list) > 0:
    del guest_list[len(guest_list) - 1]


print(f"\n{guest_list}")

