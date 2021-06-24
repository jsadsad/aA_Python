A common Python technique is to use range(len(someList)) with a for loop to iterate over the indexes of a list. Here's an example of that.

```
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
```

will return

```
Index 0 in supplies is: pens
Index 1 in supplies is: staplers
Index 2 in supplies is: flame-throwers
Index 3 in supplies is: binders
```

_Using range(len(supplies)) in the previously shown for loop is handy because the code in the loop can access the index (as the variable i) and the value at that index (as supplies[i]). Best of all, range(len(supplies)) will iterate through all the indexes of supplies, no matter how many items it contains._

# List of lists

_Sometimes you will have a list of lists. You can loop over those and destructure at the same time just like you can do in JavaScript. As a matter of fact, Python has had this feature since its inception whereas JavaScript only recently got it._

```
l = [[1, 2], [3, 4], [5, 6]]
for a, b in l:
    print(a, ', ', b)

# Prints 1, 2
# Prints 3, 4
# Prints 5, 6
```

# For Loop with Dictionary

There are three dictionary methods that will return list-like values of the dictionary’s keys, values, or both keys and values: keys(), values(), and items(). The values returned by these methods are not true lists, they cannot be modified and do not have an append() method. But, like the range, they're list-like and can be used with a for loop.

### values()

```
spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)

# Prints red
# Prints 42
```

### keys()

```
for k in spam.keys():
    print(k)

# Prints color
# Prints age
```

### items()

```
# Getting tuples
for i in spam.items():
    print(i)

# Prints ('color', 'red')
# Prints ('age', 42)


# Destructuring to values
for k, v in spam.items():
    print('Key: ' + k + ' Value: ' + str(v))

# Prints Key: age Value: 42
# Prints Key: color Value: red
```
