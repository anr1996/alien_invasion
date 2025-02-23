response = ''

while response.lower() != 'cheese stuffed':
    response = input("\nEnter a pizza crust:\n")
    if response.lower() == 'cheese stuffed':
        print("\nWe do not have that kind of crust anymore.")
    else:
        print(f"\nAdding {response} crust to the pizza.") 
    