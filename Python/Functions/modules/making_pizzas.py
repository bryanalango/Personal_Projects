import pizza

from Codes.Functions.passing_arbitrary_arguments import make_pizza

pizza.make_pizza(16, 'peperoni')
pizza.make_pizza(12, 'mushrooms', 'green pepper', 'extra cheese')
pizza.make_pizza(18, 'coriander', 'pineapple', 'zesta', 'lemon')

print("\n")

# Using as to Give a Function an Alias

from pizza import make_pizza as mp

mp(16, 'mushroom')
mp(34, 'veges', 'hot pepper', 'white salad')

# Importing all Functions in a Module
# This can be done using the (*) operator

from pizza import *

make_pizza(18, 'pepperoni')
make_pizza(12, 'cabbage', 'kales', 'beef', 'tomatoes')