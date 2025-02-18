# How will you compare two lists ?

# Direct Comparision: if two lists are exactly the same. same elements in the same order)

l1 = [1,2,3] 
l2 = [1,2,3]

result = l1 == l2
print(result)       # print true when both lists are identical


# Check if Lists have same elements ignoring order.

l1 = [20, 30, 10]
l2 = [30, 10, 20]

result = sorted(l1)==sorted(l2)
print(result)


# Check for Common Elements between two list

l1 = ['a', 'b', 'c']
l2 = ['c', 'b', 'a']
common_element = list(set(l1)&set(l2))
print(common_element)