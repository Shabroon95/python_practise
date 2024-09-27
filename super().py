class A:
    def display(self):
        print("this is display function")
class B(A):
    def m1(self):
        print("this is m1 method")
        super().display()

obj=B()
obj.m1()

class C:
    a,b=30,20
    def m2(self, x,y):
        print(x+y)
        print(self.a+self.b)
class D(C):
    i,j=200,40
    def m3(self):
        print(self.i+self.j)
        print(self.a+self.b)
        print(super().a+super().b)

obj1=D
obj1.m3(self=obj1)
a,b=5,8
class E:
    a,b=30,20


class F(E):
    a,b=200,40
    def m4(self,a,b):
        print(a+b) # Local variables
        print(globals()['a']+globals()['b']) #global variables
        print(self.a+self.b) #class variables
        print(self.a+self.b) # class variable
        print(super().a+super().b) # parent class variables

obj2=F
obj2.m4(obj2, 50,60)

class AB:
    def __init__(self):
        print("constructor fROM A")

class x(AB):
    def __init__(self):
        print("child class constructor")
        #super(x, self).__init__()
        AB.__init__(self) # approach 2 it will also call parent class constructor

ob=x()
