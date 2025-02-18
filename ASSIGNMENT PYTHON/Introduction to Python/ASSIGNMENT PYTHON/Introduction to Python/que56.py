#  Write a Python program to map two lists into a dictionary 
#  Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}). 

l1 = ['a', 'b', 'd', 'c']
l2 = [400, 400, 400, 300]

my_dict = dict(zip(l1,l2))  # zip is designed for pairing 
print(my_dict)


l1,l2 = zip(*my_dict.items())
l1 = list(l1)
l2 = list(l2)
print(l1)
print(l2)
