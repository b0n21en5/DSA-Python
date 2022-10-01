s=0
def sum_arr(a):
    global s
    if len(a)==0:return print(s)
    s+=a[0]
    a=a[1:]
    sum_arr(a)

a=[7,4,9,11,-3]
sum_arr(a)