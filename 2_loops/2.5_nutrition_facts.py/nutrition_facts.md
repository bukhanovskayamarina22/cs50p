---
created: 2024-04-26T00:39:41 (UTC +03:00)
tags: []
source: https://cs50.harvard.edu/python/2022/psets/2/nutrition/
author: 
---

# Nutrition Facts - CS50's Introduction to Programming with Python

> ## Excerpt
> An introduction to programming using Python, a popular language for general-purpose programming, data science, web programming, and more.

---
The U.S. Food & Drug Adminstration (FDA) offers [downloadable/printable posters](https://www.fda.gov/food/food-labeling-nutrition/nutrition-information-raw-fruits-vegetables-and-fish) that “show nutrition information for the 20 most frequently consumed raw fruits … in the United States. Retail stores are welcome to download the posters, print, display and/or distribute them to consumers in close proximity to the relevant foods in the stores.”

In a file called `nutrition.py`, implement a program that prompts ~consumers~ users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit, per the [FDA’s poster for fruits](https://cs50.harvard.edu/python/2022/psets/2/nutrition/Nutrition-Information-for-Raw-Fruits---small-PDF-Poster.pdf), which is also [available as text](https://www.fda.gov/food/food-labeling-nutrition/raw-fruits-poster-text-version-accessible-version). Capitalization aside, assume that users will input fruits exactly as written in the poster (e.g., `strawberries`, not `strawberry`). Ignore any input that isn’t a fruit.

Log into [cs50.dev](https://cs50.dev/), click on your terminal window, and execute `cd` by itself. You should find that your terminal window’s prompt resembles the below:

to make a folder called `nutrition` in your codespace.

to change directories into that folder. You should now see your terminal prompt as `nutrition/ $`. You can now execute

to make a file called `nutrition.py` where you’ll write your program.

Be sure to try other fruits and vary the casing of your input. Your program should behave as expected, case-insensitively.

You can execute the below to check your code using `check50`, a program that CS50 will use to test your code when you submit. But be sure to test it yourself as well!

```
check50 cs50/problems/2022/python/nutrition
```

Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. Visit the URL that `check50` outputs to see the input `check50` handed to your program, what output it expected, and what output your program actually gave.

In your terminal, execute the below to submit your work.

```
submit50 cs50/problems/2022/python/nutrition
```
