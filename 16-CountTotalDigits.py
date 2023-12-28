 #  Write a program to count the total number of digits in a number using a while loop.
 # For example, the number is 75869, so the output should be 5.

def count_digits(number):
    return sum(1 for _ in str(number))  # Leverages generator expression for counting

# Example usage
number = 343565657
num_digits = count_digits(number)
print(f"The number {number} has {num_digits} digits.")


"""
Output

Enter a number: 
343565657
The total number of digits in the number 343565657 is: 9
"""
