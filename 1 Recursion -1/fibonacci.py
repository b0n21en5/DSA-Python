def fib(n):
    if n==2 or n==1:return 1
    return fib(n-1)+fib(n-2)
n=int(input())
print(fib(n))