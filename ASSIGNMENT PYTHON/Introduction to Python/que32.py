# Write a Python program to remove duplicates from a list.

l1 = [1, 2, 2, 3, 4, 5, 6, 4, 3, 7, 1, 1,]
uniq_lst = list(set(l1))
print(uniq_lst)


# METHOD-2
l1 = [1, 2, 2, 3, 4, 5, 6, 4, 3, 7, 1, 1,]
uniq_lst =[]

for i in l1:
    if i not in uniq_lst:
        uniq_lst.append(i)

print(uniq_lst)