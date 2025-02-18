# Write a Python script to check if a given key already exists in a dictionary. 


my_dict = {"a":1, "b":2, "c":3, "d":4}

key = input("Enter key : ")

if key in my_dict:
    print(f"key {key} is exist")
else:
    print(f"key {key} is not exist")

    
