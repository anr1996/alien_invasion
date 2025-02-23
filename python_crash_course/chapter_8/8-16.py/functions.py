

def make_car(manufacturer, model, **car_info):
    
    """retrieve the following information about a car from the user:
    manufacturer, model, car info.
    a single name for manufacturer and model is required, however car info is a dictionary
    where we can supply as many name values pairs we need to describe various pieces of data 
    about the car. """
    
    divider = "-" * 70
    print(f"Manufacturer: {manufacturer.title()}")
    print(f"Model: {model.title()}")
    
    for car, info in  car_info.items():
        print(f"{car.title()}: {info}")
    
    print(divider)