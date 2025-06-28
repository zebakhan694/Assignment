#  Write a Python program to check multiple keys exists in a dictionary 

status = True
my_dict = {"a":1, "b":2, "c":3, "d":4} 



while status:
    key = input("Enter key you want to check exist or not : ")
    if key in my_dict:
        print(f"{key} is Exist..")
    else:
        print(f"{key} is not exist..")

    choice = input("Do you want to continue.. press y for yess or n for no: ").lower()
    if choice == 'n' or choice == 'no':
        status = False
    else: 
        status = True


