---
created: 2024-04-22T19:45:24 (UTC +03:00)
tags: []
source: https://cs50.harvard.edu/python/2022/psets/1/interpreter/
author: 
---

# Math Interpreter - CS50's Introduction to Programming with Python

> ## Excerpt
> An introduction to programming using Python, a popular language for general-purpose programming, data science, web programming, and more.

---
## [Math Interpreter](https://cs50.harvard.edu/python/2022/psets/1/interpreter/#math-interpreter)

Python already supports math, whereby _you_ can write code to add, subtract, multiply, or divide values and even variables. But let’s write a program that enables _users_ to do math, even without knowing Python.

In a file called `interpreter.py`, implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as `x y z`, with one space between `x` and `y` and one space between `y` and `z`, wherein:

-   `x` is an integer
-   `y` is `+`, `-`, `*`, or `/`
-   `z` is an integer

For instance, if the user inputs `1 + 1`, your program should output `2.0`. Assume that, if `y` is `/`, then `z` will not be `0`.

Note that, just as `python` itself is an interpreter for Python, so will your `interpreter.py` be an interpreter for math!

Hints

Recall that a `str` comes with quite a few methods, per [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods), including `split`, which separates a `str` into a sequence of values, all of which can be assigned to variables at once. For instance, if `expression` is a `str` like `1 + 1`, then

```
<span>x</span><span>,</span> <span>y</span><span>,</span> <span>z</span> <span>=</span> <span>expression</span><span>.</span><span>split</span><span>(</span><span>"</span><span> </span><span>"</span><span>)</span>
```

will assign `1` to `x`, `+` to `y`, and `1` to `z`.

## [Demo](https://cs50.harvard.edu/python/2022/psets/1/interpreter/#demo)

## [Before You Begin](https://cs50.harvard.edu/python/2022/psets/1/interpreter/#before-you-begin)

Log into [cs50.dev](https://cs50.dev/), click on your terminal window, and execute `cd` by itself. You should find that your terminal window’s prompt resembles the below:

Next execute

to make a folder called `interpreter` in your codespace.

Then execute

to change directories into that folder. You should now see your terminal prompt as `interpreter/ $`. You can now execute

to make a file called `interpreter.py` where you’ll write your program.

## [How to Test](https://cs50.harvard.edu/python/2022/psets/1/interpreter/#how-to-test)

Here’s how to test your code manually:

-   Run your program with `python interpreter.py`. Type `1 + 1` and press Enter. Your program should output:
-   Run your program with `python interpreter.py`. Type `2 - 3` and press Enter. Your program should output:
-   Run your program with `python interpreter.py`. Type `2 * 2` and press Enter. Your program should output
-   Run your program with `python interpreter.py`. Type `50 / 5` and press Enter. Your program should output

You can execute the below to check your code using `check50`, a program that CS50 will use to test your code when you submit. But be sure to test it yourself as well!

```
check50 cs50/problems/2022/python/interpreter
```

Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. Visit the URL that `check50` outputs to see the input `check50` handed to your program, what output it expected, and what output your program actually gave.

## [How to Submit](https://cs50.harvard.edu/python/2022/psets/1/interpreter/#how-to-submit)

In your terminal, execute the below to submit your work.

```
submit50 cs50/problems/2022/python/interpreter
```
