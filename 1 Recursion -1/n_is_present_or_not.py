def isPresent(a,n):
    if len(a)==0:return False
    if a[0]==n:return True
    return isPresent(a[1:],n)

n=int(input())
a=[int(n) for n in input().split(' ',n-1)]
x=int(input('Type a num to check if its in list:\n'))
print(isPresent(a,x))