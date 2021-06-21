# Indexing a string

Like JavaScript, Python starts counting at zero. This is called zero-based indexing. A character in a string can be accessed with square brackets.

```
print("Spaghetti"[0]) # => S
print("Spaghetti"[4]) # => h
```

Python allows negative indexes to access a character from the end of the string. The last character is at index -1.

```
print("Spaghetti"[-1]) # => i
print("Spaghetti"[-4]) # => e
```

Additionally, Python gives shortcuts to get a series of characters by using a range. A range consists of a start value followed by a colon then an end value.

Important: The series returned does not include the end value.

```
print("Spaghetti"[1:4]) # => pag
print("Spaghetti"[4:-1]) # => hett
print("Spaghetti"[4:4]) # => (empty string)
```

A shortcut for the beginning of the string is to omit the first number.

```
print("Spaghetti"[:4]) # => Spag
print("Spaghetti"[:-1]) # => Spaghett
```

A shortcut for the end of the string is to omit the second number.

```
print("Spaghetti"[1:]) # => paghetti
print("Spaghetti"[-4:]) # => etti
```

If a single index is requested which is not in the string, then an error occurs.

```
print("Spaghetti"[15]) # => IndexError: string index out of range
print("Spaghetti"[-15]) # => IndexError: string index out of range
```

_However, ranges do not error._

```
print("Spaghetti"[:15]) # => Spaghetti
print("Spaghetti"[15:]) # => (empty string)
print("Spaghetti"[-15:]) # => Spaghetti
print("Spaghetti"[:-15]) # => (empty string)
print("Spaghetti"[15:20]) # => (empty string)
```
