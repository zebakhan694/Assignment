# write a python program to generate and print a list of first and last 5 elements 
# where the values are square of numbers between 1 and 30.

l1 = []   

for i in range(1,31):
    if i<=5 or i>25:
        l1.append(i*i)
print(l1)

    