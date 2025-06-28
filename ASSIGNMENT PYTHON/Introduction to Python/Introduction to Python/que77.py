# Write a Python program to read a file line by line store it into a variable. 

with open("sample.txt","r") as file:
    data = file.read()  # read entire file into a variable
    print(data)