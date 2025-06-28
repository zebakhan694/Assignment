# Write a python program to find the longest words.

file = open("sample.txt","r")
words = file.read().split()  # read the file and split it innto words

longest_word = max(words,key=len)
print(longest_word)
 
   
    