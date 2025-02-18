#  Write a Python program to count the frequency of words in a file. 

with open("sample.txt", "r") as file:
    data = file.read().split()      # split the line into words
    print(len(data))