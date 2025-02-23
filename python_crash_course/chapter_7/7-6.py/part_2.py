# pizza Toppings

in_stock = True

while in_stock:
    response = input("\nEnter a pizza topping:\n")
    
    if response.lower() == 'quit':
        in_stock = False
    else:
        print(f"\nAdding {response} to the pizza.")