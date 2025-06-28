#  Write a Python program to create a dictionary from a string. 
#  Note: Track the count of the letters from the string.

status = True
my_dict = {}

while status:
    key = input("Enter Key : ")
    my_dict[key] = len(key)

    choice = input("do you want to continiue.. press y for yes or n for no : ").lower()
    if choice == 'n' or choice == 'no':
        status = False
    else: 
        status = True

print(my_dict)