import emp,pickle
f=open("emp.dat","wb")
n=int(input("enter no of employees"))
for i in range(n):
    no=int(input("enter no"))
    name=input("enter name")
    sal=float(input("enter sal"))
    addr=input("enter addr")
    e=emp.Employee(no,name,sal,addr)
    pickle.dump(e,f)
