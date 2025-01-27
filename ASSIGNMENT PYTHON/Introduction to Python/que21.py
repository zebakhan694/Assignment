# Write a Python program to add 'in' at the end of a given string(length should be at least 3).
# If the given sting is already ends with 'ing' then add 'ly' instead if the string lenght of the given string is less than 3,
# leave iot unchanged.


string = input("Enter a string : ")
if len(string)>=3:
    if string.endswith("ing"):
        result = string + 'ly'
    else:
        result = string + 'in'
else:
    result = string

print(result)