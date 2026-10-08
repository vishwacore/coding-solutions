# Enter your code here. Read input from STDIN. Print output to STDOUT
A=list(map(int,input().split()))
B=list(map(int,input().split()
))
result=[]
for a in A:
    for b in B:
        print((a,b),end=" ")
