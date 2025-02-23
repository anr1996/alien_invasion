# pizza Toppings


while True:
    response = input("\nEnter a pizza topping:\n")
    
    if response.lower() == 'quit':
        break
    else:
        print(f"\nAdding {response} to the pizza.")