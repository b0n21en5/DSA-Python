
def sum_arr(a):

    if len(a)==0:return 0

    return a[0] + sum_arr(a[1:])
    
n=int(input())
a=[int(n) for n in input().split(' ',n-1)]
print(sum_arr(a))