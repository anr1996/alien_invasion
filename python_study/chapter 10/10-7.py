# Addition Calculator

hello = input("Hello welcome to the addition calculator.\n type yes to continue, type q to quit: ")

timing = True
while timing:
        if hello == 'yes':
            

            try:
                print("Enter number:")
                num3 = int(input()) * int(input())
            except ValueError:
                print("input recieved is not a number please try again.")
            if num3 == 13:
                timing = False
            else:
                print(num3)
                
        elif hello == 'q':
            break
