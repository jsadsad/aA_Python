Because Python is whitespace-aware and uses indentations for its blocks, the designer of the language decided that there needs to be a special indicator to show that the clause of a code block is empty. Hence, the pass keyword has been part of the language since the beginning.

```
if True:
  pass
```

```
while True:
  pass
```

You must use `pass` to have syntactically correct code. For example, the following code will fail with an IndentationError and the message "expected an indented block".

```
# THIS CODE WILL RESULT IN AN IndentationError
print("Hello")

if True:

print("Good-bye")
```

The two code blocks above look like this in Python.
For all statements that have a colon at the end of them, you must signify that they're empty by using the pass keyword if you do not provide a clause for them. That includes if, while, def, and all the other ":" blocks that you will encounter.
