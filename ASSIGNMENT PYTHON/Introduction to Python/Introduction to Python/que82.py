#  Write a Python program to copy the contents of a file to another file.

file1 = open("file1.txt", "r")
file2 = open("file2.txt", "w")

for i in file1:
    file2.write(i)

print("File conent is copied successfully")