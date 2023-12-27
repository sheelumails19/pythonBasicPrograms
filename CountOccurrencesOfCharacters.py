"""
Exercise 10: Write a program to count occurrences of all characters within a string
Given:
str1 = "Apple"
Expected Outcome:
{'A': 1, 'p': 2, 'l': 1, 'e': 1}
"""

def count_occurrences(s):
    # Initialize an empty dictionary to store character counts
    char_count = {}

    # Iterate through each character in the string
    for char in s:
        # If the character is already in the dictionary, increment its count
        if char in char_count:
            char_count[char] += 1
        # Otherwise, add the character to the dictionary with a count of 1
        else:
            char_count[char] = 1

    return char_count

def main():
    # Given string
    str1 = "Apple"
    
    # Get the character counts
    result = count_occurrences(str1)
    
    # Print the result
    print(result)

if __name__ == "__main__":
    main()

"""
Output
{'A': 1, 'p': 2, 'l': 1, 'e': 1}
"""
