# Join

A common request is to take a list and join them together into a single string. Often a separator is needed to make the data look pretty. Often this is a space, comma, line break; or perhaps a dash in the case of zip codes and phone numbers.

In Javascript the join function was available on arrays. In Python, however, this is flipped around. The join function is actually on strings.

This means that ''.join(sequence) connects the elements in the sequence using the character inside the single quotes is between each element.

```
shopping_list = ['bread','milk','eggs']
print(','.join(shopping_list))
bread, milk, eggs
```

# Format

Python has a very powerful formatting engine for making exactly the strings you need. The format function is one way to apply these options. Like `join`, `format` is applied to strings.
