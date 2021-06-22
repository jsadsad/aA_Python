"""
This is a simple script to practice creating a few functions in Python

Please follow the steps outlined below.
"""

# STEP 1 - Write a function named `welcome` that prints a welcome message


def welcome(str):
    print("hello % s" % (str))


# Step 2 - Write a function named `calc_sum` that
#   - takes in two numbers and
#   - returns their sum


def calc_sum(num1, num2):
    return num1 + num2


# DO NOT EDIT - The guts of the program
welcome("josh")
print(calc_sum(1, 2), "is 3?", calc_sum(1, 2) == 3)
print(calc_sum(-10, -2), "is -12?", calc_sum(-10, -2) == -12)
print(calc_sum(1.1, -2.2), "is -1.1?", calc_sum(1.1, -2.2) == -1.1)
print(calc_sum("a", "b"), "is ab?", calc_sum("a", "b") == "ab")
print(calc_sum([1, 2], [3, 4]), "is [1,2,3,4]?", calc_sum([1, 2], [3, 4]) == [1, 2, 3, 4])
