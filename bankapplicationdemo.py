import sys
class Customer:
    bankname='DURGABANK'
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
    def deposite(self,amt):
        self.amt=amt
        return self.balance+self.amt
    def withdraw(self,amt):
            self.amt=amt
            return self.balance-self.amt

c=Customer('sagar',10000)
name=input('enter your name')
while True:
    print('welcome to',Customer.bankname)
    option=input('what do you want type D for deposite, W for withdraw,e for exit')
    if option =='D' or option=='d':
        amt=float(input('enter amount you want to deposite'))
        d=c.deposite(amt)
        print('your balance is',d)
    elif option=='w' or option=='W':
        amt=float(input('enter amount you want to withdraw'))
        d=c.withdraw(amt)
        print('your balance after withdraw',d)
    elif option =='e' or option=='E':
        print('thamks for banking')
        sys.exit()
    else:
        print('invalid option')

