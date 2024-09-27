class myclass:
    def m1(self):
        print("Good morning")
    def __init__(self):
        print("This is constructor") # constructor will call when we initiate the object

obj=myclass()
obj.m1()

class A:
    def __init__(self, val1, val2):
        print(val1) #local variables
        print(val2)
        self.val1 = val1 # converting as class variables
        self.val2 = val2
    def Add(self):
        print(self.val1+self.val2)

obj1=A(100,200)
obj1.Add()

class Myclass:
    def m1(self):
        print("this is methos m1")
        self.m2(100)

    def m2(self, a):
        print("this is m2 methos",a)

obj2=Myclass()
obj2.m1()

class B:
    name="Ansar"
    def __init__(self, name): # constructor argument is local variable
        print(name)
        print(self.name) #represents the class variables

ob=B("shabroon")

class Emp:
    def __init__(self, eid,ename,sal):
        self.eid=eid
        self.ename=ename
        self.sal=sal

    def display(self):
        print("EMPID:{} EMPname:{} EMPSal:{}".format(self.eid,self.ename,self.sal))
        print("EmpId:%d, Empname:%s, Empsal:%g", self.eid,self.ename, self.sal)

obj3=Emp(10,"Shabroon",10000)
obj3.display()