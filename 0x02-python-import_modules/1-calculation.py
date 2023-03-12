#!/usr/bin/python3

# Import the necessary functions from the '1-calculation.py' file
from 1-calculation import add, sub, mul, div

if __name__ == "__main__":
    # Define the values of 'a' and 'b'
    a = 10
    b = 5

    # Use the imported functions to perform the desired calculations
    # and print the results
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
