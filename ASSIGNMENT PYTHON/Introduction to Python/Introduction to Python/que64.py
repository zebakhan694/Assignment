#  Write a Python function that checks whether a passed string is palindrome or not



def is_palindrome(str):
    rev = str[::-1]
    return rev == str
    


string = input("Enter a String : ")
if is_palindrome(string):
    print("palindrome")
else:
    print("not a palindrome")

