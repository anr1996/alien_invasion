class Restuarant:
    def __init__(self, restuarant_name, cuisine_type):
        self.name = restuarant_name
        self.cuisine = cuisine_type
    
    def describe_restuarant(self):
        print(f"Restuarant name: {self.name.title()}")
        print(f"Cuisine type: {self.cuisine.title()}")
        
    def open_restuarant(self):
        print(f"The restuarant '{self.name.title()}' is now open!")
        

luigi_restuarant = Restuarant("Luigi's Place", 'Italian')

divider = "-" * 60
print(f"\n{divider}")

luigi_restuarant.describe_restuarant()
print("\n")

luigi_restuarant.open_restuarant()
print(divider)

