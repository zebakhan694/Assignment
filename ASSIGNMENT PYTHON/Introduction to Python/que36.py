# write a python function that takes a list and returns a new list with unique elements of the first list.

def unique_elements(l1,unq_lst):
    for i in l1:
        if i not in unq_lst:
            unq_lst.append(i)
    print(unq_lst)


l1 = [1, 2, 3, 4, 2, 3, 5, 6, 1, 4]
unq_lst = []

unique_elements(l1,unq_lst)


