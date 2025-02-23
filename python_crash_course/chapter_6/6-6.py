# polling

print("\n")

registered_voters = {}

potential_voters = ['adrian',
                    'michael',
                    'andrea',
                    'jessica',
                    'brandon',
                    'cassandra',
                    'hilary',
                    'jarian',
                    'matt',
                    ]

while True:
    
    key = ''
    value = ''
    
    key = input(f"\nEnter your name into the poll for your favorite computer language:\n\n")
    if key.lower() == 'exit':
        break
    
    value = input(f"\nEnter your favorite computer language\n\n")
    if value.lower() == 'exit':
        break
    registered_voters[key] = value


print("\n")

for voters in potential_voters:
    if voters.lower() not in registered_voters.keys():
        print(f"{voters.title()}, Please taken part in the poll. your opinion matters.\n")
        
    elif voters.lower() in registered_voters.keys():
        print(f"thank you {voters.title()} for taking part in the poll!\n")

for voters in registered_voters:
    if voters not in potential_voters:
        print(f"thank you {voters.title()} for taking part in the poll!\n")
  
    
