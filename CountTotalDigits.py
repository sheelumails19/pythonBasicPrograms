 #  Write a program to count the total number of digits in a number using a while loop.
 # For example, the number is 75869, so the output should be 5.

def count_digits(number):
    # Initialize count to 0
    count = 0
    
    # Loop until the number becomes 0
    while number != 0:
        # Increment count by 1 for each digit
        count += 1
        # Remove the last digit from the number
        number //= 10
    
    return count

def main():
    # Take input from the user
    num = int(input("Enter a number: "))
    
    # Count the number of digits
    num_digits = count_digits(num)
    
    # Print the result
    print(f"The total number of digits in the number {num} is: {num_digits}")

if __name__ == "__main__":
    main()


"""
Output

Enter a number: 
343565657
The total number of digits in the number 343565657 is: 9
"""
