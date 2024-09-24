class Restaurant: 
    
    # defining init method and storing two variables.
    def __init__(self, name, food): 
        self.name = name
        self.food = food
        self.number_served = 400

    # defining function, calling for variable 'name'
    def introduce(self):    
        print(f"{self.name} has amazing food")

    # defining functon, calling for variable 'food'
    def type_food(self):
        print(f" Our {self.food} is the best italian food around")

    def customers_served(self):
        print(f"{self.number_served} customers served today")

    def customer_update(self, update):
        if self.number_served >= update:
            print("we are getting busy")
        elif self.number_served < update:
            print("we need more customers!")

    def customer_increase(self, customer_increase):
        self.number_served += customer_increase

    def get_descriptive_name(self):
        long_name = f"{self.name} {self.food}"
        return long_name.title()


my_restaurant = Restaurant("Johnny's", 'southern italian blend')

print(f"welcome to {my_restaurant.name}")

# creating instance
my_restaurant.introduce()

print(f"if you like a {my_restaurant.food} you will enjoy our food!")

# creating instance
my_restaurant.type_food() 

my_restaurant.customer_update(100)
my_restaurant.customers_served()

my_restaurant.customer_increase(200)
my_restaurant.customers_served()


class IceCream_stand(Restaurant):
    """represent new restaurant ice cream stand"""

    def Introductory_statement(self):
        print(f"Welcome to {self.name}, we serve {self.name}.")

    def __init__(self, name, food):
        super().__init__(name, food)

    def My_flavors(self, flavors):
        flavors = ['chocolate', 'vanilla', 'strawberry']
        print(f"My flavors are {flavors}")

My_Icecream = IceCream_stand("Riches Ice-Cream, ", 'Real ice cream.')
print(My_Icecream.get_descriptive_name())
My_Icecream.My_flavors(1)


# 9-7 Admin.














