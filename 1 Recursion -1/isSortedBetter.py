def isSorted(a,i):
    if i==len(a) or i==len(a)-1:return print('Sorted')
    if a[i]>a[i+1]:return print('not Sorted')
    return isSorted(a,i+1)
a=[1,4,5,6,8,11,78]
isSorted(a,0)