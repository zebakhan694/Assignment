# write a python program to unzip a list of tuples into individual lists

l1 = [(1,"a"),(4,'c'),(7,'d')]
l2,l3 = zip(*l1)
l2 = list(l2)
l3 = list(l3)

print(l1)
print(l2)
print(l3)
