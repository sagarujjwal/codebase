'''class P:
    def property(self):
        print('Gold+Land+Cash+Power')
    def marry(self):
        print('Appalamma')
class C(P):
    def marry(self):
        #super().marry()
        print('Katrina Kaif')

c=C()
c.property()
c.marry()
'''


class Loan:
    def interestrate():
        return 10.50
class Gold(Loan):
    def interestrate():
        return 14.00
class Car(Loan):
    def interestrate():
        return 6.00
c=Car()
print(c.interestrate())
g=Gold()
print(g.interestrate())
