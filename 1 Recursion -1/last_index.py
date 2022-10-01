def lastIndex(a, n, i):
    if i < 0: return print('num is not the in list')
    if a[i] == n: return print(i)
    return lastIndex(a, n, i - 1)


def last_index(a, n):
    li = len(a) - 1
    if len(a) == 0: return -1
    if a[li] == n: return li
    res = last_index(a[0:li], n)
    if res == -1:return -1
    else:return res


def lastIndexB(a,n,i):
    if i==len(a):return -1
    res = lastIndexB(a,n,i+1)
    if res!=-1:return res
    else:
        if a[i]==n:return i
        else:return -1


def last_indexB(a,n):
    if len(a)==0:return -1
    res = last_indexB(a[1:],n)
    if res !=-1:return res+1
    else:
        if a[0]==n:return 0
        else:return -1


a = [3, 4, 1, 5, 3, 5, 7, 15, 4, 8, 9, 9, 3, 7]
n = int(input('Enter num to check its index: '))
lastIndex(a, n, len(a) - 1)
print(last_index(a, n))
print(lastIndexB(a,n,0))
print(last_indexB(a,n))