"""
Write a program to use string.format() method to format the following three variables as per the expected output 

Given: 
totalMoney = 1000 
quantity = 3 
price = 450 

Expected Output: 

I have 1000 dollars so I can buy 3 football for 450.00 dollars.
"""


def main():
    totalMoney = 1000
    quantity = 3
    price = 450.00

    # Format the variables using string.format() method
    output = "I have {} dollars so I can buy {} football for {:.2f} dollars.".format(totalMoney, quantity, price)

    # Print the formatted string
    print(output)

if __name__ == "__main__":
    main()

"""
Output
I have 1000 dollars so I can buy 3 football for 450.00 dollars.
"""
