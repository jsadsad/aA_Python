# Solution 1
def difference(list):
    mn = min(list)
    mx = max(list)
    return mx - mn


# Solution 2
def difference(lst):
    max = lst[0]
    min = lst[0]
    for i in range(1, len(lst)):
        val = lst[i]
        if val < min:
            min = val
        if val > max:
            max = val
    return max - min


print(difference([10, 15, 20, 2, 10, 6]))
# 20 - 2 = 18

print(difference([-3, 4, -9, -1, -2, 15]))
# 15 - (-9) = 24

print(difference([4, 17, 12, 2, 10, 2]))
# 17 - 2 = 15
