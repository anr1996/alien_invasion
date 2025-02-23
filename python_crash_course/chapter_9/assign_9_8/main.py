from classes import *

divider = "_" * 60

user_1 = Admin('adrian', 'rich', location = "keizer", age = 28)


print(divider)
print("\nAdmin info:\n")
user_1.describe_user()

print("\nAdmin privileges:\n")
user_1.privileges.show_privileges()
print(divider)