class Restaurant:
    def __init__(self, cuisine_specialty, service_hours, name):
        self.cuisine_specialty = cuisine_specialty
        self.service_hours = service_hours
        self.name = name
        self.food_menu = ['tacos', 'burritos', 'enchiladas', 'taquitos', 'chips and salsa']
        self.drink_menu = ['mhargarita', 'modelo', 'coors light', 'water', 'tea', 'lemonade']
        self.weekly_sales = 10_000
    
    def welcome(self):
        print(f" welcome to {self.name} !")

    def food_type(self):
        """list of different foods"""
        print(f"Here is our food menu:\n {self.food_menu}.")

    def drink_types(self):
        """list of different drinks"""
        print(f"here is our drink menu:\n {self.drink_menu} ")

    def business_hours(self):
        """business hours"""
        print(f"Here are our hours of business:\n {self.service_hours}")

    def moneyss(self):
        print(f"{self.weekly_sales}")

""" 
my_business = Restaurant('Mexican cuisine', 'monday - friday, 10am - 8pm', 'Johnnys')
my_business.welcome()
my_business.business_hours()
my_business.food_type()
my_business.drink_types()
print(f"\n")

response = input("would you like to see our weekly sales so far?: ")
if response == 'yes':
    my_business.moneyss()
else:
    print("okay nevermind then")
 """
