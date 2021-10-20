def digcount(n,c):
    if n==0:
        return c
    else:
        n=n//10
        return digcount(n,c+1)
n=int(input())
print(digcount(n,0))
