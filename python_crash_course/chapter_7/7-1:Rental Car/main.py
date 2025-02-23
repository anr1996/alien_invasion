# Rental Car

toyota_desc = "A Japanese brand known for its reliable and efficient vehicles."

ford_desc = ("An American company famous for pioneering assembly line production and " + 
"producing popular models like the Mustang.")

volkswagen_desc = ("A German automaker best known for the Beetle and its role in the " + 
"mass production of affordable cars.")

honda_desc = ("Another Japanese car manufacturer, known for the Civic and Accord, as " + 
              "well as their advancements in engine technology.")

bmw_desc = " A luxury German brand, renowned for its sporty and performance-oriented vehicles."

chevrolet_desc = ("An American brand, often called Chevy, and known for models like " + 
                  "the Camaro and Silverado.")

mercedes_benz_desc = ("A premium German automaker famous for luxury vehicles, " + 
                      "including the S-Class and GLE.")

hyundai_desc = ("A South Korean manufacturer that has gained a strong reputation for " + 
                "affordability and warranty offers.")

tesla_desc = ("An American electric vehicle and clean energy company founded by " + 
              "Elon Musk, known for its innovative use of technology.")

volvo_desc = ("A Swedish brand known for its emphasis on safety and recently, a focus " + 
"on electric and hybrid vehicles.")






car_list = {
    "toyota" : toyota_desc,
    "ford" : ford_desc,
    "volkswagen" : volkswagen_desc,
    "honda" : honda_desc,
    "bmw" : bmw_desc,
    "chevrolet" : chevrolet_desc,
    "mercedes benz" : mercedes_benz_desc,
    "hyundai" : hyundai_desc,
    "tesla" : tesla_desc,
    "volvo" : volvo_desc,
    }
response = input("\nEnter the name of the car you would like to rent today:\n")


car_found = False
for car, car_type in car_list.items():
    if car.lower() == response.lower():
        car_found = True
        print(f"\nCar selected:\n{car.title()}.\n")
        print(f"Car description:\n{car_type}\n")
        break

if car_found == False:
    print("\nWe do not have that car in stock.\n")
    
    