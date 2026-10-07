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
