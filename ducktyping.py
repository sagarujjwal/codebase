class Cat:
    def talk(self):
        print('meao meao meao')
class Dog:
    def talk(self):
        print('bho bho bho')
class Duck():
    def talk(self):
        print('duck duck duck')

class Human:
    def walk(self):
        print('walking')


def f1(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    elif hasattr(obj,'walk'):
        obj.walk()

t1=Cat()
f1(t1)
t2=Dog()
f1(t2)
t3=Human()
f1(t3)
