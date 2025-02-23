sum = 0

try:
    num = int(input("Enter a number\n"))

except ValueError:
    print("That is not a number!")

else:
    sum += num
    
try:
    num = int(input("\nEnter a number\n"))

except ValueError:
    print("That is not a number!")

else:
    sum += num
    print(f"\nThe sum of the two numbers is {sum}")