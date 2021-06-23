# Write a function using the and operator that returns the Boolean result of the and operator being applied to the function's arguments.
# Write your function, here.
def And(bool_1, bool_2):
    return bool_1 and bool_2


print(And(True, False))  # > False
print(And(True, True))  # > True
print(And(False, True))  # > False
print(And(False, False))  # > False
