# How Do You Check the Presence of a Key in A Dictionary? 

my_dict = {"a":1, "b":2, "c":3, "d":4}

key = input("Enter Key which you want to check the presence in a dictionary : ")

if key in my_dict:
    print(f"key {key} is present...")
else:
    print(f"key {key} is not present...")