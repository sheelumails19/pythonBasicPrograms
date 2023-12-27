// Description: Write a function that finds the longest word in a given sentence.
  
def find_all_longest_words(sentence):
    words = sentence.split(' ')
    longest_length = max(len(word) for word in words)
    return [word for word in words if len(word) == longest_length]
 
# Example usage
sentence = "The quick brown fox jumped overrt the lazy dog"
longest_words = find_all_longest_words(sentence)
 
print("Longest words:", longest_words)
 
// Output: Longest words: ['jumped', 'overrt']
