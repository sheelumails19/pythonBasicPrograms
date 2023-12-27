person = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

# Creating a new dictionary by unpacking the original dictionary
# and adding/modifying key-value pairs
updated_person = {**person, 'age': 31, 'job': 'Developer'}

# Printing the updated dictionary
print(updated_person)


// Output: {'name': 'John', 'age': 31, 'city': 'New York', 'job': 'Developer'}
