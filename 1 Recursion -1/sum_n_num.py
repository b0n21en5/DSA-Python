def sum(n):
    if n==0:
        return 0
    else:
        return n + sum(n-1)
n = int(input())
print(f'Sum of {n} natural num is: {sum(n)}')