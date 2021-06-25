# Write your function, here.
def find_smallest_num(list):
    return min(list)


# Solution 2
def find_smallest_num(lst):
    smallest = lst[0]
    for i in range(1, len(lst)):
        value = lst[i]
        if value < smallest:
            smallest = value
    return smallest


print(find_smallest_num([34, 15, 88, 2]))  # > 2
print(find_smallest_num([34, -345, -1, 100]))  # > -345
print(find_smallest_num([-76, 1.345, 1, 0]))  # > -76
print(find_smallest_num([0.4356, 0.8795, 0.5435, -0.9999]))  # > -0.9999
print(find_smallest_num([7, 7, 7]))  # > 7
