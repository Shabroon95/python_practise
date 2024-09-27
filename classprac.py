class Myclass:
    def myfunc(self):  # By default it is an instance method
        pass

    def mydisplay(self, Name):
        print("Name of the function parameter", Name)


mc = Myclass()
mc.myfunc()

mc.mydisplay("shabroon")


class Myclass1:

    def m1(self):  # instace methos we can using class object
        print("by default it's an instance method")

    @staticmethod  # static method we can call directly with class
    def m2(self):
        print("it is an static method, by using keyword @static method", self)


mc1 = Myclass1()
mc1.m1()
Myclass1.m2(10)
i, j = 25, 10


class Myclas2:
    a = 200
    b = 300

    def myfunc(self):
        #print(X)  # local variables
        print(i + j)  # global variables
        print(self.a + self.b)  # class variables we can access through self keyword

    def mul(i,j):
        print(i * j)
        #print(self.a * self.b)
        print(globals()['i']+ globals()['j']) # when both local and gloabl variable are same then we have to use this function



x = Myclas2
x.mul(10, 10)
