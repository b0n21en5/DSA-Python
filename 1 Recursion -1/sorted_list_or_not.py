def isSorted(l):
    a=len(l)
    if a==0 or a==1:return True
    if l[0]>l[1]:return False
    list_f = l[1:]
    chek = isSorted(list_f)

    if chek:return True
    else:return False

l = [1,332,43,44,45,99]
print(isSorted(l))