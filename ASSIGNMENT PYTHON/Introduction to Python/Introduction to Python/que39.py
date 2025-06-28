# Write a Python program to find the second smallest number in a list

def second_smallest(nums):
    unique_num=list(set(nums))    # remove duplicates
    if len(unique_num)<2:
        return None    # not enough unique elements
    unique_num.sort()
    return unique_num[1]

numbers = [2,4,9,8,0,6,2]
result = second_smallest(numbers)

if result is not None:
    print(f"{result} is a second smallest number")
else:
    print("List does not have second smallest number")