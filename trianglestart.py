size=10
n=size*2-2
b=0
for i in range(size):
    for j in range(n):
        print(" ",end='')
    n-=1
    for j in range(i):
        print(b,end=" ")
    b+=1
    print()
