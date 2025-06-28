# Write a Python function to reverse a string if its length is a multiple of 4.

def reverse(str):
    rev = str[::-1]
    if len(str)%4==0:
        print(rev)

str = input("Enter a string : ")
reverse(str)







