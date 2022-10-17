
# 9-10
# importing module Restaurant from MyRestaurant
from MyRestaurant import Restaurant

# defining variables for Restaurant.
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

