class A:
    def mydisplay():
        print("This is parent calss")

class B(A):
    def m2():
        print("this is m2 method from parent calss")

obj=A
#obj.mydisplay()

obj1=B
obj1.mydisplay()
obj1.m2()

class x:
    x, y =10,20
    def m1(self):
        print()
