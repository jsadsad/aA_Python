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

## Comma as thousands separator

`print('{:,}'.format(1234567890))` returns `'1,234,567,890'`

## Date and Time

```
d = datetime.datetime(2020, 7, 4, 12, 15, 58)
print('{:%Y-%m-%d %H:%M:%S}'.format(d))
```

returns `'2020-07-04 12:15:58'`

## Percentage

```
points = 190
total = 220
print('Correct answers: {:.2%}'.format(points/total))
```

returns `Correct answers: 86.36%`

## Data Table

```
width=8
print(' decimal      hex   binary')
print('-'*27)
for num in range(1,16):
    for base in 'dXb':
        print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
    print()
```

returns

```
decimal      hex   binary
---------------------------
       1        1        1
       2        2       10
       3        3       11
       4        4      100
       5        5      101
       6        6      110
       7        7      111
       8        8     1000
       9        9     1001
      10        A     1010
      11        B     1011
      12        C     1100
      13        D     1101
      14        E     1110
      15        F     1111
```
