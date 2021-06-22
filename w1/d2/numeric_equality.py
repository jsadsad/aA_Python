# Write your function, here.
def is_same_num(num_1, num_2):
    # return num_1 is num_2
    return num_1 == num_2


# The Equality operator (==) compares the values of both the operands and checks for value equality. Whereas the ‘is’ operator checks whether both the operands refer to the same object or not.

# is checks for the same memory locations.


print(is_same_num(4, 8))  # >  False
print(is_same_num(2, 2))  # >  True
print(is_same_num(2, "2"))  # >  False
