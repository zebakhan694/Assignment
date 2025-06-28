#  Write a Python program to count the number of lines in a text file. 

with open("sample.txt", "r") as file:
    data = file.readlines()
    print(len(data))