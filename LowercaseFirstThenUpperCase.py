"""
Exercise 4: Arrange string characters such that lowercase letters should come first
Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.
Given:
str1 = PyNaTive

Expected Output:
yaivePNT
"""

def arrange_characters(s):
    # Initialize empty strings for lowercase and uppercase letters
    lowercase = ""
    uppercase = ""
    
    # Separate the characters of the string based on their case
    for char in s:
        if char.islower():
            lowercase += char
        else:
            uppercase += char
    
    # Concatenate the two strings to get the desired order
    arranged_str = lowercase + uppercase
    
    return arranged_str

def main():
    # Given string
    str1 = "PyNaTive"
    
    # Get the arranged string
    result = arrange_characters(str1)
    
    # Print the result
    print(f"The arranged string is: {result}")

if __name__ == "__main__":
    main()

"""
Output
The arranged string is: yaivePNT
"""
