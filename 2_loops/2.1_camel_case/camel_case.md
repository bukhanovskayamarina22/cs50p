---
created: 2024-04-23T21:55:30 (UTC +03:00)
tags: []
source: https://cs50.harvard.edu/python/2022/psets/2/camel/
author: 
---

# camelCase - CS50's Introduction to Programming with Python

> ## Excerpt
> An introduction to programming using Python, a popular language for general-purpose programming, data science, web programming, and more.

---
In some languages, it’s common to use [camel case](https://en.wikipedia.org/wiki/Camel_case) (otherwise known as “mixed case”) for variables’ names when those names comprise multiple words, whereby the first letter of the first word is lowercase but the first letter of each subsequent word is uppercase. For instance, whereas a variable for a user’s name might be called `name`, a variable for a user’s first name might be called `firstName`, and a variable for a user’s preferred first name (e.g., nickname) might be called `preferredFirstName`.

Python, by contrast, [recommends](https://peps.python.org/pep-0008/#function-and-variable-names) [snake case](https://en.wikipedia.org/wiki/Snake_case), whereby words are instead separated by underscores (`_`), with all letters in lowercase. For instance, those same variables would be called `name`, `first_name`, and `preferred_first_name`, respectively, in Python.

In a file called `camel.py`, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.

Log into [cs50.dev](https://cs50.dev/), click on your terminal window, and execute `cd` by itself. You should find that your terminal window’s prompt resembles the below:

to make a folder called `camel` in your codespace.

to change directories into that folder. You should now see your terminal prompt as `camel/ $`. You can now execute

to make a file called `camel.py` where you’ll write your program.

You can execute the below to check your code using `check50`, a program that CS50 will use to test your code when you submit. But be sure to test it yourself as well!

```
check50 cs50/problems/2022/python/camel
```

Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. Visit the URL that `check50` outputs to see the input `check50` handed to your program, what output it expected, and what output your program actually gave.

In your terminal, execute the below to submit your work.

```
submit50 cs50/problems/2022/python/camel
```
