# for loop
lst = [1, "2", "three", True, None]

new_list = []

for l in lst:
    new_list.append(l)

# print("for loop list:", new_list)

# [value for-loop] / list comprehension
value_list = [el for el in lst]

# print("value for loop list:", value_list)

# copying .map()
to_map_list = ["diana", "helen", "josh", "michelle"]

mapped_list = []
for l in to_map_list:
    mapped_list.append(l.title())

# print(mapped_list)

# copying filter()

to_filter_list = [1, 10, 11, 12, 30, 100, 90]

filtered_list = [n for n in to_filter_list if n % 3 == 0]

# print(filtered_list)

# it is second nature to write in list comprehension for python

# creating a tupple

letters = ["a", "b", "c"]
nums = [1, 2]

tupple_list = []
for l in letters:
    for n in nums:
        tupple_list.append((n, l))

## creating a tupple with list comprehension
tupple_list_comprehension = [(n, l) for n in nums for l in letters]

# print(tupple_list_comprehension)
# print(tupple_list)

## dictionary comprehension
keys = ["age", "name", "fav_food"]
values = [26, "JC", "sushi"]

# for loop
# d = dict()
# # d = {} # is also acceptable
# for i in range(len(keys)):
#     d[keys[i].title()] = values[i]


# dictionary comprehension
d = {keys[i].title(): values[i] for i in range(len(keys))}

# more python way
# this is destructuring
d = {key: value for key, value in zip(keys, values)}

print(d)
