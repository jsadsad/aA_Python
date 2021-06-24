# Functions that use iterables

1. Filter

   - filter(function, iterable) creates a new iterable of the same type which includes each item for which function returns True.
   - function: takes an item (from the iterable) and returns a Boolean
   - iterable: e.g. list, tuple, range, dictionary, set, or str

2. Map

   - map(function, iterable) creates a new iterable of the same type which includes the result of calling the function on every item in the iterable.
   - function: takes an item (from the iterable) and returns another item (of same or different type)
   - iterable: e.g. list, tuple, range, dictionary, set, or str

3. Sorted

   - sorted(iterable, key=None, reverse=False) creates a new sorted list from the items in iterable
   - iterable: e.g. list, tuple, range, dictionary, or set
   - key: optional function which converts an item to a value to be compared (e.g. key=str.lower for case-insensitive sorting on a list of strings)

```
 a = ("h", "b", "a", "c", "f", "d", "e", "g")
 x = sorted(a, reverse=True)
 print(x)
```

4. Enumerate

   - enumerate(iterable, start=0) starts with a sequence and converts it to a series of tuples. Each tuple is made up of two elements: index and value.

   - The parameter start must be set using its name and an equal sign.

   - The best way to understand enumerate is to consider an example.

   ```
   quarters = ['First', 'Second', 'Third', 'Fourth']
   print(enumerate(quarters))
   print(enumerate(quarters, start=1))
   (0, 'First'), (1, 'Second'), (2, 'Third'), (3, 'Fourth')
   (1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Fourth')
   ```

5. zip

   - zip(\*iterables) creates a zip object filled with tuples that combine 1-to-1 the items in each provided iterable. If the iterables have uneven length then zip stops when the shortest one runs out of items.

# Functions that analyze iterables

1. len()
2. max()
3. min()
4. sum()
5. any()
6. all()

# Working with dictionaries

Python has a special function that is very useful when working with dictionaries.

`dir`
`dir(dictionary)` returns the list of keys in the dictionary.

It can also be used on objects or modules to return a list of their attributes.
