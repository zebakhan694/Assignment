# Write a Python function to check whether a number is in a given range

def checkrange(num):
    if num>=0 and num<=100:
        print("Valid Number")
    else:
        print("Invalid Number")


print("Number must be in 0 to 100")
num = int(input("Enter a Number : ")) 
checkrange(num)
