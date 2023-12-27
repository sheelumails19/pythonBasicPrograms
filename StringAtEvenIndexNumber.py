// For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.


# Given string
str_value = "pynative"

# Loop through the string using a step of 2 (for even indices)
for index in range(0, len(str_value), 2):
    print(str_value[index])

"""
Output:
p
n
t
v
"""
