# Write a python program to check whether a list contains a sub list.

def contain_sublist(main_list,sub_list):
    if not sub_list:
        return True     # Empty sublist is always considered to be present
    n,m = len(main_list),len(sub_list)
    for i in range(n-m+1):
        if main_list[i:i+m]==sub_list:
            return True
    return False


main = [1,2,3,4,5]
sub = [3,4]

if contain_sublist(main,sub):
    print("sublist found!")
else:
    print("sublist not found!")