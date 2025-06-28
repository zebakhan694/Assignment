# How can you get a random number in python? 

import random

random_value = random.randint(1,101)    # 1 - 100
print(random_value)

random_value = random.randrange(1, 100, 5) # between 1 to 99 and pick a multiple of 5
print(random_value)