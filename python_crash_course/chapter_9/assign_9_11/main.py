from classes import Admin

user_1 = Admin('Adrian', 'Rich', location = "Keizer", age = 28)

divider = "_" * 60
print(f"{divider}\n")
print("admin privileges:\n")
user_1.privileges.show_privileges()
print(divider)
