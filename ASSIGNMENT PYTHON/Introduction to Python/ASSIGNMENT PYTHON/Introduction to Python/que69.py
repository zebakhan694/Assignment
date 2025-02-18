#  How will you set the starting value in generating random numbers? 

import random

random.seed(10)   # Setting the seed value

print(random.randint(1,100))   # Generating a randome number between 1-100
print(random.randint(1,100))   # Generating the same sequence if the seed is fix
