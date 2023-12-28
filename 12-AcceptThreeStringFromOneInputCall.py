# Write a program to take three names as input from a user in the single input() function call.

names = input("Enter three names separated by spaces: ").split()
if len(names) != 3:
    print("Please provide exactly three names.")
else:
    print("Names entered:")
    for name in names:
        print(name)

"""
Output 

Enter three names separated by spaces: 
sag raj there
Names entered:
sag
raj
there
"""
