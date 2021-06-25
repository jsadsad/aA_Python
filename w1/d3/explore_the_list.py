# DO NOT EDIT - Starting with a simple lists of colors and numbers
colors = ["blue", "Green", "PURPLE", "blue-green", "sky blue"]
numbers = [2, 34, 8.5, -22.0, 33 // 4, 2 ** 5]
print("COLORS", colors)
print("NUMBERS", numbers)

# 1. Print the total number of colors (length of the list)
print("number of colors:", len(colors))

# 2. Print the first color
print("first color:", colors[0])


# 3. Print the second and third colors
print("second color: % s and third color: % s" % (colors[1], colors[2].lower()))


# 4. Print the last two colors
print("third color: % s and last color: % s" % (colors[-2], colors[-1].lower()))


# 5. Print the smallest number in the numbers list
print(min(numbers))


# 6. Print the largest number in the numbers list
print(max(numbers))


# 7. Sort the numbers
numbers = sorted(numbers)


# UNCOMMENT WHEN YOU WORK ON #7
print("SORTED NUMBERS", numbers)

# 8. Sort the colors alphabetically ignoring case
colors = sorted(colors, key=str.lower)

# UNCOMMENT WHEN YOU WORK ON #8
print("SORTED COLORS", colors)
