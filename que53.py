# Write a Python script to print a dictionary where the keys are numbers between 1 and 15. 

my_dict = {i:i**2  for i in range(1,16)}   # we assinging squre of the key as a value
print("Generated dictionary : ",my_dict)


my_dict = {}
for i in range(1,16):
    my_dict[i] = i**3                # we assinging cube of the key as a value
print("Generated dictionary : ",my_dict)