# Write a Python program to count the number of strings where the string lenght is 2 or more and
# the first and last character are same from a given lists of strings.

str = input("Enter Any String : ")


if len(str)>=2:
    if str[0] == str[-1]:
        print(len(str))
    else:
        print("First and Last charachter of string are not same")
else:
    print("string lenght is less than 2 characters")
