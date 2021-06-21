# Duck-typing

If it looks like a duck and quacks like a duck, then it must be a duck.

Duck typing is a programming style which avoids checking an object's "type" to figure out what it can do. In other words, duck-typing avoids tests for type() or isinstance().

Instead a method or attribute is simply called or used in the code. If necessary a check would be for hasattr(). This approach is also known as EAFP: Easier to ask for forgiveness than permission

By focusing on interfaces, duck-typing makes well-designed code more flexible.

Python uses duck-typing as its fundamental approach.

```
count = max = min = 0
print(count)           # => 0
print(max)             # => 0
print(min)             # => 0
```

The value - and even the type - of a variable can be reassigned at any time.

```
a = 17
print(a) # => 17
a = 'seventeen'
print(a) # => seventeen
```

_Unlike JavaScript, Python will not return NaN as the result of calculations; instead, it throws exceptions._

```
a = '7'
a /= 2
print(a)

TypeError: unsupported operand type(s) for /=: 'str' and 'int'
```

_Python's replacement for null is None. It is used to indicate a variable has no value._

`None` is very special because it is actually an object (of type `NoneType`). That means it can be used wherever other objects are used.

```
my_var = None
```

And it is just as easy to find out if the value of a variable is None.

```

print(my_var is None)     # => True
```

## Why use Python's None type?

There are many cases when you may use None.

Often you will want to perform an action that may or may not work. Using None is one way you can check what happened.

For example, maybe you are loading optional instructions from a file. If that file in not found, the instructions variable's value could remain None. Then later in your code you check instructions is not None so the program knows whether to display those instructions or skip that step.
