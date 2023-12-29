"""
Write a program to remove characters from a string starting from zero up to n and return a new string.
For example:
	• remove_chars("pynative", 4) so output must be tive. Here, we need to remove the first four characters from a string.
	• remove_chars("pynative", 2) so output must be native. Here, we need to remove the first two characters from a string.
Note: n must be less than the length of the string.

"""

def remove_chars(s, n):
    # Check if n is valid (less than the length of the string)
    if n >= len(s):
        return "n must be less than the length of the string."
    
    # Return the string after removing the first n characters
    return s[n:]

# Test the function with examples
print(remove_chars("pynative", 4))  # Output: tive
print(remove_chars("pynative", 2))  # Output: native

"""
Output:
tive
native
"""
