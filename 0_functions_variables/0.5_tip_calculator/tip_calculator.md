---
created: 2024-04-22T16:52:03 (UTC +03:00)
tags: []
source: https://cs50.harvard.edu/python/2022/psets/0/tip/
author: 
---

# Tip Calculator - CS50's Introduction to Programming with Python

> ## Excerpt
> An introduction to programming using Python, a popular language for general-purpose programming, data science, web programming, and more.

---
In the United States, it’s customary to leave a tip for your server after dining in a restaurant, typically an amount equal to 15% or more of your meal’s cost. Not to worry, though, we’ve written a tip calculator for you, below!

```python
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO


def percent_to_float(p):
    # TODO


main()
```

Well, we’ve written _most_ of a tip calculator for you. Unfortunately, we didn’t have time to implement two functions:

Assume that the user will input values in the expected formats.

Log into [cs50.dev](https://cs50.dev/), click on your terminal window, and execute `cd` by itself. You should find that your terminal window’s prompt resembles the below:

to make a folder called `tip` in your codespace.

to change directories into that folder. You should now see your terminal prompt as `tip/ $`. You can now execute

to make a file called `tip.py`. Copy and paste the code above into a file, and complete the implementations of `dollars_to_float` and `percent_to_float`, replacing each `TODO` with one or more lines of your own code.

You can execute the below to check your code using `check50`, a program that CS50 will use to test your code when you submit. But be sure to test it yourself as well!

```
check50 cs50/problems/2022/python/tip
```

Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. Visit the URL that `check50` outputs to see the input `check50` handed to your program, what output it expected, and what output your program actually gave.

In your terminal, execute the below to submit your work.

```
submit50 cs50/problems/2022/python/tip
```
