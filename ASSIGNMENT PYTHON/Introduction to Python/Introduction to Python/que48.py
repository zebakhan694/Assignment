# write a python script to sort (ascending to discending) a dictionary by value.

dictionary = {"ronak":3, "reema":2, "zeba":4,  "aashu":1}

sorted_dict = dict(sorted(dictionary.items(), key= lambda item : item[1]))
print(sorted_dict)

