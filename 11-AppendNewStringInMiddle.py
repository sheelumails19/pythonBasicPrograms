"""
Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
Given:
s1 = "Ault"
s2 = "Kelly"
Expected Output:
AuKellylt
"""

def append_in_middle(s1, s2):
    return s1[:len(s1) // 2] + s2 + s1[len(s1) // 2:]

s1 = "Ault"
s2 = "Kelly"
result = append_in_middle(s1, s2)
print(f"The new string is: {result}")


"""
Output
The new string after appending 'Kelly' in the middle of 'Ault' is: AuKellylt
"""
