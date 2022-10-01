def firstIndex(a,n,i):
    if len(a)==i:return print('num is not the in list')
    if a[i]==n:return print(i)
    return firstIndex(a,n,i+1)

    
def first_index(a,n):
    if len(a)==0:return -1
    if a[0]==n:return 0
    res = first_index(a[1:],n)
    if res==-1:return -1
    else:return res+1


a= [3,4,5,3,5,7,4,8,9,9,3,7]
n=int(input('Enter num to check its index: '))
firstIndex(a,n,0)
print(first_index(a,n))