# write a Python function that takes two lists and returns true if they have at least one common member.

def common_member(l1,l2):
    if list(set(l1)&set(l2)):
        return True
    else:
        return False


l1 = [3, 4, 5]
l2 = [1, 2, 3]    

result = common_member(l1,l2)
print(result)

    
