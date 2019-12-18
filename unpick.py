import emp,pickle
f=open('emp.dat','rb')
print("emp details")
while True:
    try:
        
        obj=pickle.load(f)
        print(obj)
        obj.display()
    except:
        print("processed all files")
        break
f.close()        

