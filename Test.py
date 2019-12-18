def display(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for k,v in kwargs.items():
          print(k,"=",v)


display(n1=10,n2=20,n3=30)
display(rno=100,name="Durga",marks=70,subject="Java")


