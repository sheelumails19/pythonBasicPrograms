# Description: Merge two sorted arrays into a single sorted array.
 
 
def merge_sorted_arrays(arr1, arr2):
    # Concatenate the two arrays
    merged_array = arr1 + arr2
 
    # Sort the merged array in ascending order
    merged_array.sort()
 
    return merged_array
 
# Example usage
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
 
merged_array = merge_sorted_arrays(arr1, arr2)
print("Merged and Sorted Array:", merged_array)
 
# Output: Merged and Sorted Array: [1, 2, 3, 4, 5, 6, 7, 8]
