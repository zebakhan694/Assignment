"""
Write a Python program to combine values in python list of dictionaries. 
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 
300}, o {'item': 'item1', 'amount': 750}] 

Expected Output: 
• Counter ({'item1': 1150, 'item2': 300})
"""

dict1 = {'item': 'item1', 'amount': 400}
dict2 = {'item': 'item2', 'amount': 300}
dict3 = {'item': 'item1', 'amount': 750}

merge_dict = [{**dict1},{**dict2},{**dict3}]
print(merge_dict)

print(type(merge_dict))