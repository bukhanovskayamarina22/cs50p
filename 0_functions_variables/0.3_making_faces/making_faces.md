---
created: 2024-04-22T16:42:53 (UTC +03:00)
tags: []
source: https://cs50.harvard.edu/python/2022/psets/0/faces/
author: 
---

# Making Faces - CS50's Introduction to Programming with Python

> ## Excerpt
> An introduction to programming using Python, a popular language for general-purpose programming, data science, web programming, and more.

---
Before there were emoji, there were [emoticons](https://en.wikipedia.org/wiki/List_of_emoticons), whereby text like `:)` was a happy face and text like `:(` was a sad face. Nowadays, programs tend to convert emoticons to emoji automatically!

In a file called `faces.py`, implement a function called `convert` that accepts a `str` as input and returns that same input with any `:)` converted to 🙂 (otherwise known as a [slightly smiling face](https://emojipedia.org/slightly-smiling-face/)) and any `:(` converted to 🙁 (otherwise known as a [slightly frowning face](https://emojipedia.org/slightly-frowning-face/)). All other text should be returned unchanged.

Then, in that same file, implement a function called `main` that prompts the user for input, calls `convert` on that input, and prints the result. You’re welcome, but not required, to prompt the user explicitly, as by passing a `str` of your own as an argument to `input`. Be sure to call `main` at the bottom of your file.

Execute `cd` by itself in your terminal window. You should find that your terminal window’s prompt resembles the below:

to make a folder called `faces` in your codespace.

to change directories into that folder. You should now see your terminal prompt as `faces/ $`. You can now execute

to make a file called `faces.py` where you’ll write your program.

You can execute the below to check your code using `check50`, a program that CS50 will use to test your code when you submit. But be sure to test it yourself as well!

```
check50 cs50/problems/2022/python/faces
```

Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. Visit the URL that `check50` outputs to see the input `check50` handed to your program, what output it expected, and what output your program actually gave.

In your terminal, execute the below to submit your work.

```
submit50 cs50/problems/2022/python/faces
```
