"""
Write a program to find how many times substring “Emma” appears in the given string.
Given:
str_x ="Emma is good developer. Emma is a writer"
Expected Output:
Emma appeared 2 times
"""

def count_substring_occurrences(main_string, substring):
    # Using count() method to count occurrences
    count = main_string.count(substring)
    
    return f'"{substring}" appeared {count} times.'

# Given string
str_x = "Emma is good developer. Emma is a writer"

# Substring to search for
substring = "Emma"

# Get and print the count of the substring occurrences
print(count_substring_occurrences(str_x, substring))

"""
Output:
"Emma" appeared 2 times.
"""
