
divider = "-" * 70
print(divider)

def make_car(manufacturer, model, **car_info):
    
    print(f"Manufacturer: {manufacturer.title()}")
    print(f"Model: {model.title()}")
    
    for car, info in  car_info.items():
        print(f"{car.title()}: {info}")
    
    print(divider)

make_car('toyota', 'corolla', color = 'red', transmission = 'automatic')
make_car('tesla', 'roadster', color = 'black', transmission = 'manual', fuel = 'electric' )
make_car('subaru', 'outback', color = 'blue', tow_package = True)




    