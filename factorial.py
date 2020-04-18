# factorial
def num(n):
    y=1
    if n==0:
        return 1
    for i in range(1,n):
        x=i
        y*=x
    return y

#print(num(0))


# factorial recursive

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

print(fact(5))
