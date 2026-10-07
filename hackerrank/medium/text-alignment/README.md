# Text Alignment

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

In Python, a string of text can be aligned *left, right* and *center*.

__.ljust(width)__

This method returns a left aligned string of length *width*.

	>>> width = 20
	>>> print 'HackerRank'.ljust(width,'-')
    HackerRank----------  

---    
__.center(width)__

This method returns a centered string of length *width*.

	>>> width = 20
	>>> print 'HackerRank'.center(width,'-')
    -----HackerRank-----

---
__.rjust(width)__

This method returns a right aligned string of length *width*.

	>>> width = 20
	>>> print 'HackerRank'.rjust(width,'-')
    ----------HackerRank
    
---
__Task__

You are given a partial code that is used for generating the _HackerRank Logo_ of variable _thickness_.  
Your task is to replace the blank (`______`) with *rjust, ljust* or *center*.




**Input Format**

 A single line containing the _thickness_ value for the logo.
 
 __Constraints__  

The *thickness* must be an *odd* number.  
$ 0 < thickness < 50$

**Output Format**

Output the desired logo.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-07T16:37:31.979Z  

```py
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())


for i in range(n):
    print(("H" * (2 * i + 1)).center(n * 2 - 1))


for i in range(n + 1):
    print(("H" * n).center(n * 2) +
          ("H" * n).center(n * 6))


for i in range((n + 1) // 2):
    print(("H" * (n * 5)).center(n * 6))


for i in range(n + 1):
    print(("H" * n).center(n * 2) +
          ("H" * n).center(n * 6))


for i in range(n):
    print(("H" * (2 * (n - i) - 1)).rjust(n * 6-(i+1)))

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/text-alignment/problem)