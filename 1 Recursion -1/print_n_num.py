def print_n_1(n):
    if n==0:return
    print(n)
    print_n_1(n-1)
def print_1_n(n):
    if n==0:return
    print_1_n(n-1)
    print(n)
n=int(input())
# print_n_1(n)
print_1_n(n)