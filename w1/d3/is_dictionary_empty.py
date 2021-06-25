# Write your function, here.
def is_empty(dictionary):
    return len(list(dictionary)) == 0


# Solution 2
def is_empty(d):
    return not d


print(is_empty({}))  # > True
print(is_empty({"a": 1}))  # > False
