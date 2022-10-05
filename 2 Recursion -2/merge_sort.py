def merge(a1,a2,a):
    i=j=k=0
    while i<len(a1) and j<len(a2):
        if a1[i]<a2[j]:
            a[k]=a1[i]
            i+=1
            k+=1
        else:
            a[k]=a2[j]
            j+=1
            k+=1
    while i<len(a1):
        a[k]=a1[i]
        i+=1
        k+=1
    while j<len(a2):
        a[k]=a2[j]
        j+=1
        k+=1

def mergeSort(a):
    if len(a)==0 or len(a)==1:return
    mid = len(a)//2
    a1 = a[:mid]
    a2 = a[mid:]

    mergeSort(a1)
    mergeSort(a2)
    merge(a1,a2,a)

a=[22,7,110,44,3,8,1,9,33,0,2]
mergeSort(a)
print(a)