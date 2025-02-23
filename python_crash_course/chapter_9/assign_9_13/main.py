from Die_class import Die

divider = "_" * 60

print(f"{divider}\n")
die_1 = Die()

for i in range(10):
    print("\n")
    die_1.roll_die()

print("\n")
print(f"{divider}\n")

die_1.set_sides(10)

for i in range(10):
    print("\n")
    die_1.roll_die()

print("\n")

print(f"{divider}\n")
die_1.set_sides(20)

for i in range(10):
    print("\n")
    die_1.roll_die()

print("\n")
print(f"{divider}\n")