#  Write a Python program to read last n lines of a file. 

file = open("sample.txt","r")
data = file.readlines()
print(data[-1])