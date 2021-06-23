# Write your function, here.
def first_before_second(s, first, second):
    return s.rindex(first) < s.index(second)


## Here's another variant, with the while loop
def first_before_second_while(s, first, second):
    first_last_index = 0
    second_first_index = 0
    i = 0
    while i < len(s):
        if s[i] == first:
            first_last_index = i
        i += 1
    i = 0
    while i < len(s):
        if s[i] == second:
            second_first_index = i
            break
        i += 1
    return first_last_index < second_first_index


print(first_before_second("a rabbit jumps joyfully", "a", "j"))
print(first_before_second("knaves knew about waterfalls", "k", "w"))
print(first_before_second("happy birthday", "a", "y"))
print(first_before_second("precarious kangaroos", "k", "a"))

print(first_before_second_while("a rabbit jumps joyfully", "a", "j"))
print(first_before_second_while("knaves knew about waterfalls", "k", "w"))
print(first_before_second_while("happy birthday", "a", "y"))
print(first_before_second_while("precarious kangaroos", "k", "a"))
