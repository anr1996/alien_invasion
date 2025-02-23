from classes import *

icecream = IcecreamStand('johns icecream', 'icecream')
icecream.get_flavors()

icecream.add_flavor('coffee')
icecream.get_flavors()

icecream.add_flavor('vanilla')
icecream.get_flavors()

icecream.add_flavor('rocky road')
icecream.get_flavors()

icecream.add_flavor('chocolate')
icecream.get_flavors()

icecream.reset_list()
icecream.get_flavors()

user_icecream_list = [
                        "Vanilla", 
                        "Chocolate", 
                        "Strawberry", 
                        "Mint Chocolate Chip", 
                        "Cookies and Cream", 
                        "Rocky Road", 
                        "Pistachio", 
                        "Butter Pecan", 
                        "Neapolitan", 
                        "Coffee",
]

icecream.add_list(user_icecream_list)
icecream.get_flavors()
    