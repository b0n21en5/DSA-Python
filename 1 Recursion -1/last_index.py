def lastIndex(a,n,i):
    if i<0:return print('num is not the in list')
    if a[i]==n:return print(i)
    return lastIndex(a,n,i-1)

    
a= [3,4,1,5,3,5,7,15,4,8,9,9,3,7]
n=int(input('Enter num to check its index: '))
lastIndex(a,n,len(a)-1)