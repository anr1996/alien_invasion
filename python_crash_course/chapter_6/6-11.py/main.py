usa_fact = ("Portland is known for its strong counterculture and is often called the" + 
"'City of Roses' for its many rose gardens, " + 
"the most famous being the International Rose Test Garden.")

thai_fact = ("Munich is renowned for hosting the annual Oktoberfest beer festival, " + 
               "which attracts millions of tourists from around the world each year. " +
               "It is also a major center for art, technology, finance, publishing, " + 
               "culture, innovation, education, business, and tourism in Germany.")

germany_fact = ("Bangkok holds the record for the world's longest city "+ 
               "name according to the Guinness World Records. The ceremonial name of " + 
               "Bangkok is Krung Thep Mahanakhon Amon Rattanakosin Mahinthara Yuthaya " + 
               "Mahadilok Phop Noppharat Ratchathani Burirom Udomratchaniwet Mahasathan " + 
               "Amon Piman Awatan Sathit Sakkathattiya Witsanukam Prasit.")

cities = {
    "portland": {
        "country" : "united states",
        "population" : 652_503,
        "cool fact" : usa_fact,
        },
    
    "bangkok": {
        "country" : "thailand",
        "population" : 1_000_000,
        "cool fact" : thai_fact,
        },
    
    "munich": {
        "country" : "germany",
        "population" : 1_470_000,
        "cool fact" : germany_fact,
        },
}

divider = "-" * 70
print(divider)
for city, info in cities.items():
    print(f"\nCity: \n{city.title()}\n")
    print(f"Country: \n{info["country"].title()}\n")
    print(f"Population: \n{info["population"]}\n")
    print(f"Cool fact: \n{info["cool fact"]}\n\n")
    print(divider)
    
    
