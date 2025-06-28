#  Write a Python script to merge two Python dictionaries 

dict1 = {'a':1, 'b':2, 'c':3}
dict2 = {'d':4, 'e':5, 'f':6}

# METHOD-1
merge_dict = {**dict1,**dict2}
print(merge_dict)


# METHOD-2
merge_dict = {}
for i in (dict1,dict2):
    merge_dict.update(i)
print(merge_dict)