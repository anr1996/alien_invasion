
# defining class 'dog'
""" class Dog:
    """"A simple attempt to model a dog.""""

    # defining method '_init_'
    def __init__(self, name, age):
       """"Initialize name and age attributes.""""
        self.name = name
        self.age = age

    # defining method 'sit'
    def sit(self):
        """"Simulate a dog sitting in a response to a command""""
        print(f"{self.name} is now sitting")

    # defining method 'roll_over'
    def roll_over(self):
        """"simulate rolling in response to a command.""""
        print(f"{self.name} rolled over!")

# assigning values to variable 'my_dog'
my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"MY dog is {my_dog.age} years old.")

# calling methods
my_dog.sit()
my_dog.roll_over()
 """



# defining class dog
""" class Dog:
   """"A simple attempt to model a dog.""""

    # defining method '_init_'
    def __init__(self, name, age):
       """"Initialize name and age attributes.""""
        self.name = name
        self.age = age

    # defining method 'sit'
    def sit(self):
        """"Simulate a dog sitting in a response to a command""""
        print(f"{self.name} is now sitting")

    # defining method 'roll_over'
   def roll_over(self):
        """"simulate rolling in response to a command.""""
        print(f"{self.name} rolled over!")


    # creating multiple instances
my_dog = Dog('willie', 3)
your_dog = Dog('lucy', 3)

print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\n")

print(f"Your dogs name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()


print("\n")
print("\n")
print("\n")
 """
# 9-1
# Restaurant

# creating a class
""" class Restaurant: 
    
    # defining init method and storing two variables.
    def __init__(self, name, food): 
        self.name = name
        self.food = food

    # defining function, calling for variable 'name'
    def introduce(self):    
        print(f"{self.name} has amazing food")

    # defining functon, calling for variable 'food'
    def type_food(self):
        print(f" Our {self.food} is the best italian food around")

my_restaurant = Restaurant("Johnny's", 'southern italian blend')

print(f"welcome to {my_restaurant.name}")

# creating instance
my_restaurant.introduce()

print(f"if you like a {my_restaurant.food} you will enjoy our food!")

# creating instance
my_restaurant.type_food() """



# 9-2
# Three Restaurants pg 162


""" class Restaurant: 
    
    # defining init method and storing three variables. 
    def __init__(self, name, food, review): 
        self.name = name
        self.food = food
        self.review = review

    # defining function, calling for variable 'name'
    def introduce(self):    
        print(f"{self.name} has amazing food")

    # defining functon, calling for variable 'food'
    def type_food(self):
        print(f" Our {self.food} is the best italian food around")
    
    # defining function, calling for variable 'critic'
    def the_critic(self):
        print(f"{self.review} gave us 4 out of 5 stars! wow!")

    

my_restaurant = Restaurant("Johnny's", 'southern italian blend', '# 1 food critic')

print(f"welcome to {my_restaurant.name}")

# creating instance
my_restaurant.introduce()

print(f"if you like a {my_restaurant.food} you will enjoy our food!")

# creating instance
my_restaurant.type_food()

my_restaurant.the_critic()
print(f"{my_restaurant.review} approves!")

 """


# 9-3 users
# pg 162



""" class User:
    def __init__(self, first_name, last_name, email, user_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.user_name = user_name
        self.password = password


    def f_name(self):
        print(f"enter your first name.\n {self.first_name}. ")

    def l_name(self):
        print(f"enter your last name. \n {self.last_name}.")
    
    def profile_email(self):
        print(f"enter your email. \n{self.email}.")
    
    def profile_user(self):
        print(f"please create a username.\n {self.user_name}.")

    def profile_pass(self):
        print(f"please create a password.\n {self.password}.")

my_profile = User('Adrian', 'Rich', 'anrich250@gmail.com', 'thok250zzz', 'forgot1996')

print("welcome to runescape, please create a account to continue...\n")
my_profile.f_name()
print(f"{my_profile.first_name}, what a cool name!\n")

my_profile.l_name()
print(f"{my_profile.last_name}, wow are you actually {my_profile.last_name }? lol\n")

my_profile.profile_email()
print(f"{my_profile.email} is google's email right? im more of an AOL guy myself.\n")

my_profile.profile_user()
print(f"{my_profile.user_name} is available!\n")

my_profile.profile_pass()
print(f"{my_profile.password} is available!, be sure to keep it a secret.\n")
print("Please confirm if the below information is correct\n")




print(f"{my_profile.first_name}")
print(f"{my_profile.last_name}")
print(f"{my_profile.email}")
print(f"{my_profile.user_name}")
print(f"{my_profile.password}")

confirmation = input("\n( yes / no ): \n")
if confirmation == 'yes':
    print('runescape account is now created, enjoy!')
else:
    confirmation == 'no'
    print('Okay please correct the information')
 """

 # Working with Classes and Instances
""" 
 # creating class 'car'
 #defining '__init__' method with the self parameter and three other parameters.
class Car:
    """"A simple attempt to represent a car.""""

    def __init__(self, make, model, year):
        """"Initialize attributes to describe a car.""""

        self.make = make
        self.model = model
        self.year = year
    def get_descriptive_name(self):
        # defining method 'get_descriptive_name'
        """"Return a neatly formatted descriptive name.""""

        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

# creating instance from the class 'car'
my_new_car = Car('audi', 'a4', 2019)

# calling instance 'get_descriptive_name'
print(my_new_car.get_descriptive_name())
 """

# Setting a Default Value for an Attribute

""" class Car:
    """"A simple attempt to represent a car.""""

    def __init__(self, make, model, year):
        """"Initialize attributes to describe a car.""""

        self.make = make
        self.model = model
        self.year = year
        self.odemeter_reading = 0

    def get_descriptive_name(self):
        # defining method 'get_descriptive_name'
        """"Return a neatly formatted descriptive name.""""

        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odemeter(self):
        """"print a statement showing the car's mileage""""
        print(f"This car has {self.odemeter_reading} miles on it.")

# creating instance from the class 'car'
my_new_car = Car('audi', 'a4', 2019)

# calling instance 'get_descriptive_name'
print(my_new_car.get_descriptive_name())
my_new_car.read_odemeter()
 """


### modifiy attribute values ###
# Modifiying an attribute's value directly

""" class Car:
    """"A simple attempt to represent a car.""""

    def __init__(self, make, model, year):
        """"Initialize attributes to describe a car.""""

        self.make = make
        self.model = model
        self.year = year
        self.odemeter_reading = 23

    def get_descriptive_name(self):
        # defining method 'get_descriptive_name'
        """"Return a neatly formatted descriptive name.""""

        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odemeter(self):
        """"print a statement showing the car's mileage""""
        print(f"This car has {self.odemeter_reading} miles on it.")

# creating instance from the class 'car'
my_new_car = Car('audi', 'a4', 2019)

# calling instance 'get_descriptive_name'
print(my_new_car.get_descriptive_name())
my_new_car.read_odemeter() 
 """

# Modifying an attribute's value through a method
""" class Car:
    """"A simple attempt to represent a car.""""

    def __init__(self, make, model, year):
        """"Initialize attributes to describe a car.""""

        self.make = make
        self.model = model
        self.year = year
        self.odemeter_reading = 25 
    def get_descriptive_name(self):
        # defining method 'get_descriptive_name'
        """"Return a neatly formatted descriptive name.""""

        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odemeter(self):
        """"print a statement showing the car's mileage""""
        print(f"This car has {self.odemeter_reading} miles on it.")

    def update_odometer(self, mileage):
        """"Set the odometer reading to the given value.""""
        self.odometer_reading = mileage

# creating instance from the class 'car'
my_new_car = Car('audi', 'a4', 2019)

# calling instance 'get_descriptive_name'
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(25)
my_new_car.read_odemeter()   """


""" class Car:
    """"A simple attempt to represent a car.""""

    def __init__(self, make, model, year):
        """"Initialize attributes to describe a car.""""

        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 25
    def get_descriptive_name(self):
        # defining method 'get_descriptive_name'
        """"Return a neatly formatted descriptive name.""""

        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """"print a statement showing the car's mileage""""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """"Set the odometer reading to the given value.""""
        
        # if statement.
        if mileage >= self.odometer_reading: 
            self.odometer_reading = mileage

        else:
            print("You can't roll back an odometer")

# creating instance from the class 'car'
my_new_car = Car('audi', 'a4', 2019)

# calling instance 'get_descriptive_name'
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(25)
my_new_car.read_odometer()  """ 



class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""

        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 25
    def get_descriptive_name(self):
        # defining method 'get_descriptive_name'
        """Return a neatly formatted descriptive name."""

        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        
        # if statement.
        if mileage >= self.odometer_reading: 
            self.odometer_reading = mileage

        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles

# create instance from the class 'car'
my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())


my_used_car.update_odometer(23_500)
my_used_car.read_odometer()  

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
 

# 9-4 Number Served:




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


""" my_used_car.update_odometer(23_500)
my_used_car.read_odometer()  

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

 """


# 9-5 Login Attempt
class User:
    # defining init function and adding multiple attributes
    def __init__(self, first_name, last_name, email, user_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.user_name = user_name
        self.password = password
        self.login_attempts = 10
        

    # defining function f_name for first name
    def f_name(self):
        print(f"enter your first name.\n {self.first_name}. ")

    # defining function l_name for last name
    def l_name(self):
        print(f"enter your last name. \n {self.last_name}.")
    
    # defining function profile_email for email
    def profile_email(self):
        print(f"enter your email. \n{self.email}.")
    
    # defining function profile_user for username
    def profile_user(self):
        print(f"please create a username.\n {self.user_name}.")

    # defining function profile_pass for password
    def profile_pass(self):
        print(f"please create a password.\n {self.password}.")

    # defining function attempted_logins for number of login attempts
    def attempted_logins(self):
        print(f"attempts to login in: {self.login_attempts}")
    
    # defining function attempted_login_increase for increase in the number of login attempts
    def attempted_login_increase(self, login_increase):
        self.login_attempts += login_increase

    # defining function login_attempts_reset for reseting the number of login attempts to 0
    def login_attempts_reset(self):
        self.login_attempts = 0

# assigning class User to variable my_profile.
my_profile = User('Adrian', 'Rich', 'anrich250@gmail.com', 'thok250zzz', 'forgot1996')

print("welcome to runescape, please create a account to continue...\n")
my_profile.f_name()
print(f"{my_profile.first_name}, what a cool name!\n")

my_profile.l_name()
print(f"{my_profile.last_name}, wow are you actually {my_profile.last_name }? lol\n")

my_profile.profile_email()
print(f"{my_profile.email} is google's email right? im more of an AOL guy myself.\n")

my_profile.profile_user()
print(f"{my_profile.user_name} is available!\n")

my_profile.profile_pass()
print(f"{my_profile.password} is available!, be sure to keep it a secret.\n")
print("Please confirm if the below information is correct\n")



# printing variables from class User.
print(f"{my_profile.first_name}")
print(f"{my_profile.last_name}")
print(f"{my_profile.email}")
print(f"{my_profile.user_name}")
print(f"{my_profile.password}")

confirmation = input("\n( yes / no ): \n")
if confirmation == 'yes':
    print('runescape account is now created, enjoy!')
else:
    confirmation == 'no'
    print('Okay please correct the information')

    # calling instances.
    my_profile.attempted_logins()
    my_profile.attempted_login_increase(100)
    my_profile.attempted_logins()
    my_profile.login_attempts_reset()
    my_profile.attempted_logins()

 

 # Inheritance
 
 # The_ init_() Method for a Child Class
 































