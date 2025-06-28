"""
    write a python program to get single string from two given strings,separated by a space and swap 
    the first two characters of each string. 
"""

def swap_first_two_chars(str1,str2):
    if len(str1)<2 or len(str2)<2:
        return "Both strings must have at least 2 characters."
    
    # Swap the first two characters 
    new_str1 = str2[:2] + str1[2:]
    new_str2 = str1[:2] + str2[2:]

    # Combine them with a space
    result = new_str1 + " " + new_str2
    return result

string1 = "hello"
string2 = "world"

output = swap_first_two_chars(string1,string2)
print("result : ",output)