# Exceptions
# Handling the ZeroDivision Exception
# Using Try-except Blocks

""" try:
    print(5/0)

# calling try-except block for error 'ZeroDivisionError'
except ZeroDivisionError:
    # printing message for error.
    print("You can't divide by zero!")
     """

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break

    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
            print("You can't divide by 0!")
    else:
        print(answer)
        