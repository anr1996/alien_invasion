# importing module 'pizza'
""" import pizza 
# making every function from the module 'pizza' available.
# calling the function 'pizza'
pizza.make_pizza(16, 'pepperoni') 
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
 """

# importing function make_pizza_2 from module pizza
""" from pizza import make_pizza_2 
make_pizza_2(12, 'mushrooms')

# importing function make_pizza from module pizza
from pizza import make_pizza 
make_pizza(10, 'salami')

 """

""" # importing multiple functions at once from module pizza.
from pizza import make_pizza, make_pizza_2 

make_pizza(12, 'green peppers')
make_pizza_2(10, 'sausage') """



""" # Using as to Give a Function an Alias
# pg 152
from pizza import make_pizza_2 as mp # giving the alias 'mp' to function 'make_pizza_2'

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese') """


""" # Using as to Give Module an Alias
# pg 153
import pizza as p

p.make_pizza(12, 'ham')
p.make_pizza_2(10, 'pineapple') """

# importing all functions from module pizza.
from pizza import * 

make_pizza(10, 'green peppers')
make_pizza_2(13, 'beef')

# Styling functions
# pg 154


# 8-15. Printing Models.




