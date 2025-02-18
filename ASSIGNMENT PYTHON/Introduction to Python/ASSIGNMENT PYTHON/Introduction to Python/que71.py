#  What is File function in python? What are keywords to create and write file. 

"""
file handling refers to th ability to read from and write to the file stored on your computer.

it allows python programs to intract with text files, binary files and other file formates.
file handling involes opening the file, reading and writing the data to them, and then clossing them when done 
"""
# x is used for creating the file
#file = open("sample.txt",'x')

# w is use for writing in file
file = open("sample.txt","w")
file.write("Hello zeba...!!")
