# Write a program to take three names as input from a user in the single input() function call.

def main():
    # Accept three names separated by spaces
    names_input = input("Enter three names separated by spaces: ")

    # Split the input string by spaces to get individual names
    names = names_input.split()

    # If the user provides fewer or more than three names, inform them
    if len(names) != 3:
        print("Please provide exactly three names separated by spaces.")
        return

    # Display the names entered by the user
    print("Names entered:")
    for name in names:
        print(name)


if __name__ == "__main__":
    main()

"""
Output 

Enter three names separated by spaces: 
sag raj there
Names entered:
sag
raj
there
"""
