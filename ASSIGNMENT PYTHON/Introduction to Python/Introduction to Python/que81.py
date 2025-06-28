#  Write a Python program to write a list to a file.

l1 = ['apple', 'banana', 'cherry', 'berry']

file = open("sample.txt", 'w')

for i in l1:
    file.write(i + "\n")

