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

japan_fact = ("Tokyo is known for its towering skyscrapers and advanced technology. " + 
              "It's also famous for having the most Michelin-starred restaurants in the world, " +
              " making it a premier destination for gastronomes.")

south_africa_fact = (" Cape Town boasts a stunning landscape including Table Mountain, " + 
                     "which is one of the New 7 Wonders of Nature. It's known for its harbor " + 
                     "and is a hotspot for biodiversity.")

austraila_fact = ("Sydney features the world-renowned Sydney Opera House with its distinctive " + 
                  "sail-like design. It is also famous for Bondi Beach, one of the most visited " + 
                  "tourist sites in Australia.")

brazil_fact = ("Rio is famous for its Carnival festival, the biggest carnival in " + 
               "the world with two million people per day on the streets. The city is also " + 
               "home to the iconic Christ the Redeemer statue, one of the New7Wonders of the World")


france_fact = ("Paris is known as the 'City of Light' (La Ville Lumière), both because of its " + 
              "leading role during the Age of Enlightenment and more literally because Paris " + 
              "was one of the first large European cities to use gas street lighting on a grand " + 
              "scale on its boulevards and monuments.")

canada_fact = ("Vancouver is renowned for its scenic beauty, surrounded by mountains " + 
               "and water. It consistently ranks as one of the world’s most livable cities and " + 
               "is a major film production center, often nicknamed 'Hollywood North.'")

cities = {
    "portland": {
        "country" : "USA",
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
    
    "tokyo": {
        "country" : "japan",
        "population" : 13_960_000,
        "cool fact" : japan_fact,
        },
    
    "cape town": {
        "country" : "south africa",
        "population" : 4_600_000,
        "cool fact" : south_africa_fact,
        },
    
    "sydney": {
        "country" : "austraila",
        "population" : 5_300_000,
        "cool fact" : austraila_fact,
        },
    
     "paris": {
        "country" : "france",
        "population" : 2_100_000,
        "cool fact" : france_fact,
        },
    
    "rio de janeiro": {
        "country" : "brazil",
        "population" : 6_700_000,
        "cool fact" : brazil_fact,
        },
    
    "vancouver": {
        "country" : "canada",
        "population" : 2_600_000,
        "cool fact" : canada_fact,
        },
    
    }

fav_list = {
    "adrian" : {
        "portland" : cities["portland"],
        "bangkok" : cities["bangkok"],
        "munich" : cities["munich"], 
        },
    
    "james" : {
        "tokyo" : cities["tokyo"],
        "cape town" : cities["cape town"],
        "sydney" : cities["sydney"], 
        
        },
    
    "jessica" : {
        "paris" : cities["paris"],
        "rio de janeiro" : cities["rio de janeiro"],
        "vancouver" : cities["vancouver"], 
        },
}





divider = "\n" + "-" * 70 + "\n"
print(divider)


for user, favourite in fav_list.items():
    
    print(f"{user.title()}'s favorite cities are:")
    for city in favourite:
        print(f"{city.title()},")
    print("\n")
    
    print("Info on each city:\n")
    
    for city, info in favourite.items():
        print(f"City: {city.title()}")
        print(f"Country: {info["country"].title()}")
        print(f"Population: {info["population"]}")
        print(f"Cool fact: {info["cool fact"].title()}\n")

    print(divider)
    
    


    
    
    
