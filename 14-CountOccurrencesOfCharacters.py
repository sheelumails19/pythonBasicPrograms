"""
Exercise 10: Write a program to count occurrences of all characters within a string
Given:
str1 = "Apple"
Expected Outcome:
{'A': 1, 'p': 2, 'l': 1, 'e': 1}
"""

from collections import Counter

def count_occurrences(s):
    return Counter(s)  # Directly create a Counter object from the string

str1 = "Apple"
result = count_occurrences(str1)
print(result)


"""
Output
{'A': 1, 'p': 2, 'l': 1, 'e': 1}
"""
