# Write your function, here.
def char_count(target, string):
    res = 0
    i = 0
    while i < len(string):
        char = string[i]
        if char == target:
            res += 1
        i += 1
    return res


print(char_count("a", "App Academy"))  # > 1
print(char_count("c", "Chamber of Secrets"))  # > 1
print(char_count("b", "big fat bubble"))  # > 4
