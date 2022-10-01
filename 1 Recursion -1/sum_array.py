s=0
def sum_arr(a):
    global s
    if len(a)==0:return print(s)
    s+=a[0]
    sum_arr(a[1:])

a=[7,4,9,21,-3]
sum_arr(a)