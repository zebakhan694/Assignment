"""
Sample string:  'w3resource'

Expected output: 
            • {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
"""

def char_frequency(s):
    freq={}
    for char in s:
        if char in freq:
            freq[char]+=1
        else:
            freq[char]=1
    return freq


sample = 'w3resource'
result = char_frequency(sample)
print(result)






