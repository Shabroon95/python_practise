class A:
    def m1(self):
        print("m1 method")

class B:
    def m2(self):
        print("this m2 method")

class c(A,B):
    def m3(self):
        print("this is m3 method")

obj = c()
obj.m1()
obj.m2()
obj.m3()


class Myclas:
    def display(self):
        print("this is display function")

class child1(Myclas):
    def display1(self):
        print("this is disp function from child1")

class child2(Myclas):
    def display2(self):
        print("this disp function from child2 ")



obj=child1
obj.display1(obj)
obj.display(obj)

obj2=child2
obj2.display2(obj2)
obj2.display(obj2)