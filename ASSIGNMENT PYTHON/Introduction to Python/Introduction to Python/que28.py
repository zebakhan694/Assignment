"""
QUE--> Difference between append() and extend() methods ?

ANS--> append(): add element to the end of the list
       extend(): add multiple elements to the end of the list
"""

l1 = [1, 2, 3, 'a', 'b']
l1.append(True)
print(l1)

l1.extend(['c','d','f'])
print(l1)
