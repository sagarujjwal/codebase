class Employee:
    def __init__(self,no,name,sal,addr):
        self.eno=no
        self.ename=name
        self.esal=sal
        self.eaddr=addr
    def display(self):
        print(self.eno,"\t",self.ename,"\t",self.esal,"\t",self.eaddr)
        
    
