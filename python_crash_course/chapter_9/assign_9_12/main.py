from admin_class import Admin

user_1 = Admin('john', 'james', location = "portland", age = 35)

divider = "_" * 60

print(f"{divider}\n")
user_1.privileges.show_privileges()
print(f"{divider}\n")