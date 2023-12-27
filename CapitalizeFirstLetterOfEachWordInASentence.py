// 	· Description: Write a function that capitalizes the first letter of each word in a sentence.
 


def capitalize_words(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())
 
# Example usage:
print(capitalize_words('this is a sentence')) 
# Output: 'This Is A Sentence'


// Output: This Is A Sentence
