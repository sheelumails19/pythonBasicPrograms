"""
Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
Given:
s1 = "Ault"
s2 = "Kelly"
Expected Output:
AuKellylt
"""

def append_in_middle(s1, s2):
    # Find the middle index of the string s1
    middle_index = len(s1) // 2
    
    # Create the new string s3 by inserting s2 in the middle of s1
    s3 = s1[:middle_index] + s2 + s1[middle_index:]
    
    return s3

def main():
    # Given strings
    s1 = "Ault"
    s2 = "Kelly"
    
    # Get the result by appending s2 in the middle of s1
    result = append_in_middle(s1, s2)
    
    # Print the result
    print(f"The new string after appending '{s2}' in the middle of '{s1}' is: {result}")

if __name__ == "__main__":
    main()

"""
Output
The new string after appending 'Kelly' in the middle of 'Ault' is: AuKellylt
"""
