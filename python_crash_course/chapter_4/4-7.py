# Threes

odd_nums = []

print("\n")

for i in range(1,31):
    num = i*3
    if num < 31:
        odd_nums.append(num)
    else:
        break
    
print("\n")
for num in odd_nums:
    print(f"{num}")

print("\n")