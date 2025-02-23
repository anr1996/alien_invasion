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
        

class IcecreamStand(Restuarant):
    
    def __init__(self, restuarant_name, cuisine_type):
        super().__init__(restuarant_name, cuisine_type)
        self.flavor_list = []
    
    def add_flavor(self, flavor):
        self.flavor_list.append(flavor)
        
    def get_flavors(self):
        
        all_flavors = 'Flavors:\n'
        for flavor in self.flavor_list:
            all_flavors += flavor + "\n"
     
        
        return print(all_flavors)
    
    def add_list(self, user_list):
        for item in user_list:
            self.flavor_list.append(item)
            
    def reset_list(self):
        self.flavor_list = []
