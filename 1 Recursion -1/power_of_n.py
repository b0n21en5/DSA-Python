def power_of_number(x, n):
    if n == 0:
        return 1
    else:
        return x*power_of_number(x, n-1)


x = int(input("Enter Any Number : "))
n = int(input("Enter power Number : "))
print(power_of_number(x, n))