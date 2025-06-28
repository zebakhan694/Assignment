#  Write a Python program to read a file line by line and store it into a list 

file = open("sample.txt", "r")
data = file.readlines()   # read the file into a list
print(data)