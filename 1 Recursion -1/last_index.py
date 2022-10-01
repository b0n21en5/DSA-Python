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


a = [3, 4, 1, 5, 3, 5, 7, 15, 4, 8, 9, 9, 3, 7]
n = int(input('Enter num to check its index: '))
lastIndex(a, n, len(a) - 1)
print(last_index(a, n))