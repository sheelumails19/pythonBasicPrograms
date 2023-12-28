# Description: Given an array containing n distinct numbers taken from 0 to n, find the one that is missing from the array.
 
def find_missing_number(nums):
    n = len(nums) + 1
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum
 
# Example usage
nums = [1, 2, 4, 6, 3, 7, 8]
print("Missing number:", find_missing_number(nums))
 
# Output: Missing number: 5
