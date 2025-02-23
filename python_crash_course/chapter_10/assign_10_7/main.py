
sum = 0

print("\n")

while True:
    try:
        num = int(input("Enter a number\n"))

    except ValueError:
        print("That is not a number!\n")

    else:
        sum += num
        break
       
while True: 
    try:
        num = int(input("\nEnter a number\n"))

    except ValueError:
        print("That is not a number!\n")

    else:
        sum += num
        print(f"\nThe sum of the two numbers is {sum}")
        break
    
