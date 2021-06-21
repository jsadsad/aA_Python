# The While Statement

Getting a block of code to execute over and over again based on some condition is also an important construct in programming. In JavaScript, you could use the while loop to do that. You can do that in Python, too!

Here is the code with a while statement:

```
spam = 0
while spam < 5:
  print('Hello, world.')
  spam = spam + 1
```

# Breaking out early

There is a shortcut to getting the program execution to `break` out of a while loop’s clause early. If the execution reaches a `break` statement, it immediately exits the while loop’s clause. In code, a `break` statement simply contains the `break` keyword. This is just like the `break` statement in JavaScript.

```
spam = 0
while True:
  print('Hello, world.')
  spam = spam + 1
  if spam >= 5:
    break

```

The while in this case is an infinite loop because while True will never have a False condition, which means it will loop forever... unless some line lets it break out of the loop. In this code, that happens at the end of the while clause where an if checks that spam is greater than or equal to 5. If it is, then the break statement runs and exits the while clause.

# Continue statements

Like break statements, continue statements are used inside loops. When the program execution reaches a continue statement, the program execution immediately jumps back to the start of the loop and reevaluates the loop’s condition. (This is also what happens when the execution reaches the end of the loop.) Here's an alternative implementation of the loop from above that uses a continue statement, as well.

```
spam = 0
while True:
  print('Hello, world.')
  spam = spam + 1
  if spam < 5:
    continue
  break
```

Here, you can see that the if statement now checks that the spam value is less than 5. If it is, then the continue statement gets executed which causes the current program statement to go back up to the while True and start the loop all over, again. When spam gets large enough to not trigger that if condition, then the break statement runs and the while loop is over.
