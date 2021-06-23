# Write your function, here.
def concat_name(str_1, str_2):
    return "% s, % s" % (str_2, str_1)


print(concat_name("First", "Last"))  # > "Last, First"
print(concat_name("John", "Doe"))  # > "Doe, John"
print(concat_name("Mary", "Jane"))  # > "Jane, Mary"

# Other solutions
# Write your function, here.
def concat_name(first_name, last_name):
    return last_name + ", " + first_name


# Here's a version that uses string formatting
def concat_name_f(first_name, last_name):
    return f"{last_name}, {first_name}"
