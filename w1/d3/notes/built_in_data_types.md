# Lists

Lists in Python are very similar to arrays in JavaScript. They are typically used to store a sequences of items that are all the same type (homogeneous).

Lists are mutable, meaning they can be changed. Primarily this means sorting, as well as adding and removing items.

Lists can be instantiated with square brackets.

`empty_list = []`
departments = ['HR','Development','Sales','Finance','IT','Customer Support']
Often you will see an empty list instantiated using the list built-in.

`specials = list()`
You can test if a value is in a list by using the in operator.

```
print(1 in [1, 2, 3]) #> True
print(4 in [1, 2, 3]) #> False
```

# Tuples

Tuples are very similar to lists in Python. The primary difference is that they are immutable, which means the tuple cannot be changed after creation.

Tuples are instantiated using parentheses.

`time_blocks = ('AM','PM')`

Although sometimes you may see tuples instantiated without parentheses.

```
colors = 'red','blue','green'
numbers = 1, 2, 3
```

Common use cases for tuples may remind you of constants.

```
weekdays = ('M','T','W','Th','F')
contactMethods = ('Email', 'SMS (Text)', 'Both')
```

You can test if a value is in a type by using the in operator.

```
print(1 in (1, 2, 3)) #> True
print(4 in (1, 2, 3)) #> False
```

# Ranges

A `range` is simply a list of numbers in order which can't be changed (immutable). Ranges are often used with for loops.

A `range` is declared using one to three parameters

start - optional (0 if not supplied) - first number in the sequence
stop - required - next number past the last number in the sequence
step - optional (1 if not supplied) - the difference between each number in the sequence

```
range(5)            # [0, 1, 2, 3, 4]
range(1,5)          # [1, 2, 3, 4]
range(0, 25, 5)     # [0, 5, 10, 15, 20]
range(0)            # [ ]
range(0, -5, -1)    # [0, -1, -2, -3, -4]
range(5, 0, -1)     # [5, 4, 3, 2, 1]
```

Notice that the stop number is NOT in the range. Range is exclusive.

# Dictionaries

A `dictionary` is a mappable collection where a hashable value (a.k.a. `hash`) is used as a key to reference an object stored in the dictionary. Dictionaries often hold arbitrary objects which are quite different (heterogenous). Dictionaries are mutable and may be changed at any time.

Often a dictionary is declared with curly braces or the dict built-in.

```
a = {'one':1, 'two':2, 'three':3}
b = dict(one=1, two=2, three=3)
c = dict([('two', 2), ('one', 1), ('three', 3)])

print(a == b)        # => True
print(a == c)        # => True
print(b == c)        # => True
print(a == b == c)   # => True
```

A useful benefit of dictionaries in Python is that it doesn't matter how the dictionary is defined, if the keys and values are the same, the dictionaries are considered equal.

Remember Dictionaries can store any kind of data:

```
complex = {
   'name': 'Bob Smith',                                  # string
   'age': 57,                                            # integer
   'weight': 215.4,                                      # float
   'height': (5, 9.5),                                   # tuple (feet, inches)
   'hobbies': {'biking', 'reading', 'playing guitar'},   # set
   'exercise_routine': [                                 # list of tuples
        ('Monday','Riding','1 hour'),
        ('Tuesday','Weightlifting','45 minutes'),
        ('Wednesday','Riding','1 hour 30 minutes'),
        ('Thursday','Walking','30 minutes'),
        ('Friday','Weightlifting','45 minutes'),
        ('Saturday','Riding','3 hours'),
        ('Sunday','',''),
    ]
}
```

You can test if a key exists in a dictionary by using the in operator.

```
print(1 in {1: "one", 2: "two"}) #> True
print("1" in {1: "one", 2: "two"}) #> False
print(4 in {1: "one", 2: "two"}) #> False
```

# Sets

A set is an unordered collection of distinct objects. Specifically, the objects need to hashable. And they will always be unique, meaning duplicate items are automatically dropped from the set.

Because of their special properties, sets have three common uses in Python

1. removing duplicates
2. membership testing (that is, finding out if an object is included)
3. mathematical operators: intersection, union, difference, symmetric difference

A standard set is mutable. Python has an immutable variation called frozenset.

Sets can be created by putting comma-separated values inside braces.

```
school_bag = {'book','paper','pencil','pencil','book','book','book','eraser'}
print(school_bag)           # => {'book','pencil','eraser','paper'}

print(1 in {1, 1, 2, 3})  #> True
print(4 in {1, 1, 2, 3})  #> False
```
