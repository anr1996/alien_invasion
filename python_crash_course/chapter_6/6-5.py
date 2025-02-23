# Rivers
country_river = {}

divider = "\n" + ('-' * 60) + "\n"
print(divider)

while True:
    country = ''
    river = ''
    
    response = input(f"\nEnter the name of the country:\n")
    if response.lower() == 'exit':
        break
    else:
        country = response
        
    response = input(f"\nEnter the name of the river that runs through this country:\n")
    if response.lower() == 'exit':
        break
    else:
        river = response
    
    country_river[country] = river
    

divider = "\n" + ('-' * 60) + "\n"
print(divider)

for river in country_river.keys():
    print(f"\nThe {country_river[river].title()} river runs through the {river.title()}.\n")

print(divider)


print("List of rivers:\n")
for river in country_river.values():
    print(f"{river.title()}\n")

print(divider)

print("List of countries:\n")
for country in country_river.keys():
    print(f"{country.title()}\n")

print(divider)
        
        
