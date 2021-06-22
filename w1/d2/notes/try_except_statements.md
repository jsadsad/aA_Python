# The problem

Your program is running along fine. Everyone is raving about how useful it is. Then, a user enters weird and unexpected data and - bam! - the code crashes and all the fun grinds to a halt.

Or someone deleted a file they thought wasn't in use. Bam! Minutes, hours or weeks later your program tries to load that file and - kaboom! - it stops again. Your phone is ringing off the hook with angry users or your boss.

All this can be prevented with proper planning and catching errors as they occur. Then your code can handle them gracefully, recover from the issue and continue providing the value the users expect.

# Catch any error

_WARNING: Use this with extreme caution, since it is easy to mask a real programming error in this way!_

An error that occurs while a program is executing is called an exception. The process of detecting these execution errors is often referred to as catching exceptions. Developers often say, "Your code threw an error," or "an exception was raised," when they are talking about exceptions that need to be caught.

The `try...except` blocks in Python work in a similar way to `if...else`. However there is nothing to check at the start. Instead try is like asking Python to listen for an error and do something with it other than crashing.

The flow enters the try block and runs each line of code in order. If there are no issues, then it skips the except block entirely. However, if one line in the try-block fails then the flow immediately skips to the start of the except block without running any more code in the try-block, including anything remaining on the line that failed.

Here's an example. Let's say you want to know how many digits are in the variable a. That variable should be a string which just happens to have numeric characters (0 through 9) in it, such as 321. As you've learned previously, you can use `len(a)` to obtain the number of characters in the string.

For the purpose of this experiment, set a to an integer so you can see the error.

```
a = 321
print(len(a))
```

Causes this output: `TypeError: object of type 'int' has no len()`
Then catch the exception by placing the try statement before the line with the error and the except statement after with at least one line of code to run as a result of the error occurring. After updating, your code may look something like this.

```
a = 321
try:
print(len(a))
except:
print('Silently handle error here')
```

```
# Optionally include a correction to the issue
a = str(a)
print(len(a))
```

Which outputs

```
Silently handle error here
3
```

# Preventing errors with duck typing

There is another approach for simple cases, such as len() from the beginning of this article, that works as well or better than try...except. In particular, think back to the "if it looks like a duck" concept (duck typing), which in this case, refers to whether the object has a way to calculate length.

If you go "under the hood" in Python, you'd find that the len() function works by calling the **len** function on the object. So any object that has **len** defined will not throw an error when len() is used with it. A number of built-in objects are already set up this way, such as str (a.k.a. string).

Checking for the existence of a property or method on an object may be performed with the hasattr function.

For example

```
# Try a number - nothing will print out
a = 321
if hasattr(a, '__len__'):
    print(len(a))

# Try a string - the length will print out (4 in this case)
b = "5555"
if hasattr(b, '__len__'):
    print(len(b))
```

Produces no errors and one output (the length of string b).

Output: `4`
