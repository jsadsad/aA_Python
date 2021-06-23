# for loop
lst = [1, "2", "three", True, None]

new_list = []

for l in lst:
    new_list.append(l)

# print("for loop list:", new_list)

# [value for-loop]
value_list = [el for el in lst]

# print("value for loop list:", value_list)

# copying .map()
to_map_list = ["diana", "helen", "josh", "michelle"]

mapped_list = []
for l in to_map_list:
    mapped_list.append(l.title())

print(mapped_list)
