---
created: 2024-04-22T19:09:15 (UTC +03:00)
tags: []
source: https://cs50.harvard.edu/python/2022/psets/1/bank/
author: 
---

# Home Federal Savings Bank - CS50's Introduction to Programming with Python

> ## Excerpt
> An introduction to programming using Python, a popular language for general-purpose programming, data science, web programming, and more.

---
In [season 7, episode 24](https://en.wikipedia.org/wiki/The_Invitations) of [Seinfeld](https://en.wikipedia.org/wiki/Seinfeld), [Kramer](https://en.wikipedia.org/wiki/Cosmo_Kramer) visits a bank that promises to give $100 to anyone who isn’t greeted with a “hello.” Kramer is instead greeted with a “hey,” which he insists isn’t a “hello,” and so he asks for $100. The bank’s manager proposes a compromise: “You got a greeting that starts with an ‘h,’ how does $20 sound?” Kramer accepts.

In a file called `bank.py`, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output `$0`. If the greeting starts with an “h” (but not “hello”), output `$20`. Otherwise, output `$100`. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

Log into [cs50.dev](https://cs50.dev/), click on your terminal window, and execute `cd` by itself. You should find that your terminal window’s prompt resembles the below:

to make a folder called `bank` in your codespace.

to change directories into that folder. You should now see your terminal prompt as `bank/ $`. You can now execute

to make a file called `bank.py` where you’ll write your program.

You can execute the below to check your code using `check50`, a program that CS50 will use to test your code when you submit. But be sure to test it yourself as well!

```
check50 cs50/problems/2022/python/bank
```

Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. Visit the URL that `check50` outputs to see the input `check50` handed to your program, what output it expected, and what output your program actually gave.

In your terminal, execute the below to submit your work.

```
submit50 cs50/problems/2022/python/bank
```
