# Movie tickets

print("Welcome to movieland.\n")

while True:
    response = input("\nEnter your age:\n")
    
    if response.lower() == 'quit':
        break
    
    response = int(response)
    
    if response < 3:
        print("\nThe ticket is free.")
        
    elif 3 <= response <= 12:
        print("\nThe ticket is $10")
    
    else:
        print("\nThe ticket is $15.")
        

