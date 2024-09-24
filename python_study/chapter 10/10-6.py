# addition.

""" num3 = int(input()) * int(input())
print(num3) """

try:
    num3 = int(input()) * int(input())
except ValueError:
    print("input recieved is not a number please try again.")
else:
    print(num3)

