# factorial
def fibonacci(n):
    a=0
    b=1
    if n==0:
        return 0
    if n==1:
        return 1
    for i in range(1,n):
        c=a+b
        print('i', i, 'a :', a, 'b :', b, 'c :', c )
        a=b
        b=c
    return c



# print(fibonacci(5))


# Recursion
def fab(n):
    if n<0:
        return ('Invalid No')
    if n==0:
        return 0
    if n==1:
        return 1
    return fab(n-1)+fab(n-2)

print(fab(9))
