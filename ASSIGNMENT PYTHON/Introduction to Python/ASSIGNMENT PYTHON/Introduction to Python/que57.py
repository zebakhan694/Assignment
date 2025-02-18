#  Write a Python program to find the highest 3 values in a dictionary 

my_dict = {'a':180, 'b':122, 'c':433, 'd':490, 'e':245, 'f':600}

result = sorted(my_dict.values(), reverse= True)[:3]
print("Highest 3 Values are --> ",result)