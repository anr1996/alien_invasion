from classes import *

divider = "_" * 60

user_1 = Admin('adrian', 'rich', location = "keizer", age = 28)


print(divider)

print("Admin info:\n")
user_1.describe_user()

print("\nadmin privileges:\n")
user_1.show_privileges()
