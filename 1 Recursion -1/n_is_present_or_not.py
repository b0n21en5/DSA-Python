def isPresent(a,n):
    if len(a)==0:return False
    if a[0]==n:return True
    return isPresent(a[1:],n)

a=[2,9,10,6,8,9,4,15]
n=int(input('Type a num to check if its in list:\n'))
print(isPresent(a,n))