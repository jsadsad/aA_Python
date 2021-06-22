print("** Doubling Penny **")

# How many times would a penny need to double to generate a million dollars?
count = 0
total = 0.01

# STEP 2: Write the while loop

while total < 10 ** 6:
    total *= 2
    count += 1


print("Double", count, "times")

# ** Doubling Penny **
# Double 28 times
# $1,342,177.28
