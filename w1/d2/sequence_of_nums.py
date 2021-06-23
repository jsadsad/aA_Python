# Write your function, here.
def seq_of_numbers(term):
    term += " "
    i = 0
    current_count = 1
    res = ""
    while i < len(term) - 1:
        if term[i] != term[i + 1]:
            res = res + str(current_count) + term[i]
            current_count = 1
        else:
            current_count += 1
        i += 1
    return res


print(seq_of_numbers("1211"))
# This is "one 1, one 2, two 1s"
# Prints "111221"

print(seq_of_numbers("111221"))
# This is "three 1s, two 2s, and one 1"
# Prints "312211"

print(seq_of_numbers("31131211131221"))
# This is "one 3, two 1s, one 3, one 1, one 2, three 1s,
#    one 3, one 1, two 2s, and one 1"
# Prints "13211311123113112211"
