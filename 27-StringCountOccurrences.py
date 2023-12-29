"""
Exercise : Write a program to count occurrences of all characters within a string
Given:
str1 = "Apple"
Expected Outcome:
{'A': 1, 'p': 2, 'l': 1, 'e': 1}
"""


str1 = "Apple"

# create a result dictionary
char_dict = dict()

for char in str1:
    count = str1.count(char)
    # add / update the count of a character
    char_dict[char] = count
print('Result:', char_dict)

"""
Output

Output:
Result: {'A': 1, 'p': 2, 'l': 1, 'e': 1}
"""
