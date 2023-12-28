"""
Write a program to find how many times substring “Emma” appears in the given string.
Given:
str_x ="Emma is good developer. Emma is a writer"
Expected Output:
Emma appeared 2 times
"""

str_x = "Emma is good developer. Emma is a writer"
substring = "Emma"
print(f'"{substring}" appeared {str_x.count(substring)} times.')

"""
Output:
"Emma" appeared 2 times.
"""
