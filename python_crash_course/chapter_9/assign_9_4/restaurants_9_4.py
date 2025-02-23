class Restuarant:
    def __init__(self, restuarant_name, cuisine_type):
        self.name = restuarant_name
        self.cuisine = cuisine_type
        self.number_served = 0
    
    def describe_restuarant(self):
        print(f"Restuarant name: {self.name.title()}")
        print(f"Cuisine type: {self.cuisine.title()}")
        
    def open_restuarant(self):
        print(f"The restuarant '{self.name.title()}' is now open!")
        
    def set_num_served(self, num_served):
        self.number_served = num_served
    
    def get_num_served(self):
        print(f"{self.number_served}")
        
    def incr_num_served(self, num_served):
        self.number_served += num_served
        
        
restuarant = Restuarant('luigis', 'italian')

divider = "-" * 60
print(divider)

restuarant.describe_restuarant()

restuarant.open_restuarant()
print(divider)

print(f"Total customers served today: {restuarant.number_served}")
restuarant.number_served = 10

print(f"Total customers served today: {restuarant.number_served}")
print(divider)

restuarant.set_num_served(20)
restuarant.get_num_served()

restuarant.incr_num_served(5)
restuarant.get_num_served()
