

def My_location_details(city, country, population='10_000'):
    if population:
        location_population = f"{city} {country} {population}"

    else:
        location_population = f"{city} {country}"
    
    return location_population.title()






