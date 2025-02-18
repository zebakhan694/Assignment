#  How Do You Traverse Through a Dictionary Object in Python?

my_dict = {"a":1, "b":2, "c":3, "d":4}

for k,v in my_dict.items():   # traverse through key and values
    print(f"{k} : {v}")
print()


for v in my_dict.values():    # traverse through values 
    print(v)
print()


for k in my_dict:              # iterate through keys
    print(k)
print()