"""
QUE--> What is list ? How will you reverse a list ?

ANS--> A list in a Python is one of the most versatile and widely used data structures.
       It is an ordered collection of an items, which can be of any data type such as numbers, strings, or even other list.
       Lists are mutable, meaning you can change thier contents after they are created.

""" 


# METHOD-1
l1 = [1, 2, 3, "zeba", "khan"]
rev=l1[::-1]
print(rev)

# METHOD-2
l1 = [1, 2, 3, "zeba", "khan"]
l1.reverse()
print(l1)

