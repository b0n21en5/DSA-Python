s=0
def sum_arr(a):
    global s
    if len(a)==0:return print(s)
    s+=a[0]
    sum_arr(a[1:])
    
n=int(input())
a=[int(n) for n in input().split(' ',n-1)]
sum_arr(a)