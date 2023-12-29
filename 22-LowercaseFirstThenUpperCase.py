"""
Exercise 4: Arrange string characters such that lowercase letters should come first
Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.
Given:
str1 = PyNaTive

Expected Output:
yaivePNT
"""

def arrange_characters(s):
    return ''.join(sorted(s, key=lambda c: not c.islower()))

# Example usage
string = "PyNaTive"
arranged_string = arrange_characters(string)
print(f"Original string: {string}")
print(f"Arranged string: {arranged_string}")


"""
Output
The arranged string is: yaivePNT
"""
