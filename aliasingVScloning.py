a=[50,50,10,40,2,4,11,1,3,45,6]
b=a
print(a)
print(b)
print(id(a))
print(id(b))
b[0]=99
print(a)
print(b)
print('''-----hello-----''')
x=[50,50,10,40,2,4,11,1,3,45,6]
y=x.copy()
print(x)
print(y)
print(id(x))
print(id(y))
y[0]=990909
print(x)
print(y)




