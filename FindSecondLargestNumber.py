#  Description: Write a function to find the second largest number in an array.
 

def second_largest_number(arr):
    unique_sorted_arr = sorted(set(arr), reverse=True)
    return unique_sorted_arr[1] if len(unique_sorted_arr) > 1 else None
 
# Example usage:
print(second_largest_number([5, 2, 7, 1, 8, 7]))
# Output: 7

# Output: 7
