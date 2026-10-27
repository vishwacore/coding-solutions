# Standardize Mobile Number Using Decorators

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Let's dive into decorators! You are given $N$ mobile numbers. Sort them in ascending order then print them in the standard format shown below:<br><br>

	+91 xxxxx xxxxx

<br>The given mobile numbers may have $+91$, $91$ or $0$ written before the actual $10$ digit number. Alternatively, there may not be any prefix at all.
<br>

**Input Format**

The first line of input contains an integer $N$, the number of mobile phone numbers. <br>
$N$ lines follow each containing a mobile number.

**Output Format**

Print $N$ mobile numbers on separate lines in the required format.

**Sample Input**

	3
    07895462130
    919875641230
    9195969878
    
**Sample Output**

	+91 78954 62130
    +91 91959 69878
    +91 98756 41230
    
**Concept**

Like most other programming languages, Python has the concept of closures. Extending these closures gives us decorators, which are an invaluable asset. You can learn about decorators in 12 easy steps [here](http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/).<br>
To solve the above question, make a list of the mobile numbers and pass it to a function that sorts the array in ascending order. Make a decorator that standardizes the mobile numbers and apply it to the function.

**Input Format**

 

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-27T17:12:53.406Z  

```py
def wrapper(f):
    def fun(l):
        f(["+91 " + c[-10:-5] + " " + c[-5:] for c in l])
        
    return fun


```

---

[View on HackerRank](https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem)