# write a Python program to test whether a passed letter is a vowel or not

# METHOD 1
letter = input("Enter a letter : ")

if letter.lower() in 'aeiou':
    print(f"{letter} is vowel")
else:
    print(f"{letter} is not a vowel")




