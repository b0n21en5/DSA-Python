def binarySearch(a,n,si,ei):
    if si>ei:return 'Not existed in list'
    mid = (si+ei)//2
    if a[mid] == n:return mid
    elif a[mid]>n:return binarySearch(a,n,si,mid-1)
    else:return binarySearch(a,n,mid+1,ei)

print(binarySearch([1,2,6,7,8,9,11,13,15,17,18,19,20],21,0,12))