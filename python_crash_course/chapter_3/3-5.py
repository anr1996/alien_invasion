# Changing Guest List:

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


