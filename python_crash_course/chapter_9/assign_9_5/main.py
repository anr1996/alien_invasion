  
# login in attempts

from classes import User

divider = "-" * 60

user_1 = User('adrian', 'rich', location = 'keizer', age = 28)

print(divider)
user_1.describe_user()


print(f"\nCurrent login attempts: {user_1.get_login()}")
user_1.incr_login()

print(f"\nCurrent login attempts: {user_1.get_login()}")
user_1.incr_login()

print(f"\nCurrent login attempts: {user_1.get_login()}")
user_1.incr_login()

print(f"\nCurrent login attempts: {user_1.get_login()}")
user_1.incr_login()


print(f"\nCurrent login attempts: {user_1.get_login()}")
user_1.reset_login()

print(f"\nCurrent login attempts: {user_1.get_login()}")
print("\n")









        
       