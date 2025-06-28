#  Write a Python program to read first n lines of a file.

file = open("sample.txt", "r")
data = file.readlines()
print(data[0])
print(data[1])
