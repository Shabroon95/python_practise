class Myclass:
    pass

#c=Myclass() # c is the reference variable
#print(c) # __main__.Myclass object at 0x00B7E4D8

#approach2

class A:
    def __str__(self):
        return "welcome"

obj=A()
print(obj)

class Emp:
    def __init__(self, eid,ename,sal):
        self.eid=eid
        self.ename=ename
        self.sal=sal
    def __str__(self):
        return "EmpID:{} EmpName:{} Empsal:{}".format(self.eid,self.ename,self.sal)



obj3=Emp(10,"Shabroon",10000)
print(obj3) #whenever we print reference variable __str__method will call
