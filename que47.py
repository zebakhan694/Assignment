# How will you create dictionary using tuples in python

tuples_list = [("name","zeba"),("city","udaipur"),("age",21)]

# METHOD-1
dictionary = dict(tuples_list)
print(dictionary)

# METHOD-2
dictionary = {key: value for key, value in tuples_list}
print(dictionary)