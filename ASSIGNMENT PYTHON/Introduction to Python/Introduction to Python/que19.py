# Write a Python program to count the occurence of each word in a given sentence.

def count_word_occurrences(sentence):
    # Convert to lowercase to make counting case-insensitive
    sentence = sentence.lower()
    
    # Remove punctuation (optional, improves accuracy)
    import string
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    
    # Split sentence into words
    words = sentence.split()
    
    # Create a dictionary to count word occurrences
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count


# Example usage
sentence = "This is a test. This test is only a test."
word_occurrences = count_word_occurrences(sentence)


# Print the results
for word, count in word_occurrences.items():
    print(f"{word}: {count}")


