The `index` function in Python is similar to the indexOf function in Javascript.

```
print("Spaghetti".index("h"))    # => 4
print("Spaghetti".index("t"))    # => 6
```

Find out how many times a substring appears in the primary string using `count`. It returns zero if the substring is not there

```
print("Spaghetti".count("h"))    # => 1
print("Spaghetti".count("t"))    # => 2
print("Spaghetti".count("s"))    # => 0
print('''We choose to go to the moon in this decade and do the other things,
not because they are easy, but because they are hard, because that goal will
serve to organize and measure the best of our energies and skills, because that
challenge is one that we are willing to accept, one we are unwilling to
postpone, and one which we intend to win, and the others, too.
'''.count('the '))                # => 4
```

Like Javascript, Python uses the addition operator (+) to stitch strings together. This can be very helpful when you want to quickly create a billion dollars. ;)

```
print("gold" + "fish")    # => goldfish
print("s"*5)              # => sssss
print("$1" + ",000"*3)     # => 1,000,000,000

```

When debugging in Python it can be very helpful to put together strings and data to figure out what's going on.

One way to do this is with the format function. You will find this in many examples and Q&A sites online.

```
first_name = "Billy"
last_name = "Bob"
print('Your name is {0} {1}'.format(first_name, last_name))  # => Your name is Billy Bob
```

In JavaScript, the join method was on the Array object. In Python, the join method is on the String object.

```
s = "--".join(["it", "is", "kind"])
print(s)

# it--is--kind
```

## Others

`isalpha()` returns True if the string consists only of letters and is not blank.
`isalnum()` returns True if the string consists only of letters and numbers and is not blank.
`isdecimal()` returns True if the string consists only of numeric characters and is not blank.
`isspace()` returns True if the string consists only of spaces, tabs, and newlines and is not blank.
`istitle()` returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters.
