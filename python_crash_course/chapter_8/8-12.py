
divider = "-" * 70

print(f"\n{divider}")

def make_pizza(*toppings):
    print(f"Making a sandwhich with the following toppings:\n")
    for topping in toppings:
        print(topping)
    print(divider)

    
        
        

make_pizza('pepperoni')

make_pizza('salami','pepperoni', 'cheese')

make_pizza('bacon', 'lettuce', 'tomato', 'mayo', 'salt', 'pepper', 'swiss cheese')
        
    