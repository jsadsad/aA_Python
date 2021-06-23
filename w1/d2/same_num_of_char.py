# Write your function, here.
def compare(str_1, str_2):
    return len(str_1) == len(str_2)


print(compare("AB", "CD"))  # > True
print(compare("ABC", "DE"))  # > False
print(compare("hello", "App Academy"))  # > False
