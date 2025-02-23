destinations = {}


while True:
    
    name = ''
    dream = ''
    
    response = input("Enter your name:\n")
    
    if response.lower() != 'quit':
        name = response
    else:
        break
    
    response = input("Enter your dream destination:\n")
    
    if response.lower() != 'quit':
        dream = response
    else:
        break
    
    destinations[name] = dream
        
print("\n")
    
for name, dream in destinations.items():
    print(f"{name.title()} Wants to visit {dream.title()}.\n")

        
    

    