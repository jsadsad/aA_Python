# Equality Operators

A quick refresher:

- > (greater than)
- > < (less than)
- > = (greater than or equal to)
- > <= (less than or equal to)
- > == (equal to)
- > != (not equal to)

Coming from JavaScript you already know how to use these!

Notice that there are only 2 equal signs for equality (equal to) and one following the exclamation point for inequality (not equal to).

_Python has a different way to handle strict comparisons: `is` and `is not`._

`is` (strictly equal to)
`is not` (not strictly equal to)

```
print (2 == '2')    # => False
print (2 is '2')    # => False
Strings are strings. It doesn't matter if they were made with double quote (") or single quote (').

print ("2" == '2')    # => True
print ("2" is '2')    # => True
Numbers, however, come in several types; for example, with or without a decimal point. The equality operator (==) considers them equal, but the identity operator (is) does not.

print (2 == 2.0)    # => True
print (2 is 2.0)    # => False
```
