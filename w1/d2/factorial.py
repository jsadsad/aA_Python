# Write your function, here.
def factorial(n):
    i = 1
    res = 1
    while i <= n:
        res *= i
        i += 1
    return res


def factorial_recursion(n):
    if n <= 2:
        return n
    return n * factorial(n - 1)


print(factorial(1))  # > 1
print(factorial(8))  # > 40320
print(factorial(12))  # > 479001600
