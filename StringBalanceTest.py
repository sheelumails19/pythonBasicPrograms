"""
Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. The character’s position doesn’t matter.
Given:
Case 1:
s1 = "Yn"
s2 = "PYnative"
Expected Output:
True
 
 
Case 2:
s1 = "Ynf"
s2 = "PYnative"
Expected Output:
False

 """

def are_strings_balanced(s1, s2):
    # Convert strings to sets of lowercase characters
    set_s1 = set(s1.lower())
    set_s2 = set(s2.lower())
    
    # Check if set_s1 is a subset of set_s2
    return set_s1.issubset(set_s2)

# Test Case 1
s1_case1 = "Yn"
s2_case1 = "PYnative"
print(are_strings_balanced(s1_case1, s2_case1))  # Expected Output: True

# Test Case 2
s1_case2 = "Ynf"
s2_case2 = "PYnative"
print(are_strings_balanced(s1_case2, s2_case2))  # Expected Output: False

"""
Output 
Output:
True
False
"""
