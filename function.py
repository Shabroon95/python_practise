def myfunc():
    pass

myfunc()

def sum(start,end):
    result=0
    for i in range(start,end+1):
        result=result+i

    return result

re=sum(1,20)
print(re)

def sum1(start,end):
    if start>end:
        print("starting number is greater than end")
        return None
    result=0
    for i in range(start,end+1):
        result=result+i

    return result

s=sum1(1,10)
print(s)

def test():
    i=100
    return

print(test())

glabal_var=25

def display():
    local_var=100
    print(glabal_var)

display()
#print(local_var) local variables we cannot access outside of the class
xy=20
def cool():
    xy=200
    print(xy)
cool()

t=20
def increment():
    #global t=10 # incorrect
    global t
    t=100
    print(t)

increment()

print(t)

def function(i,j=100): #positional arguments
    print(i,j)

function(50)
function(50,68)

import keyword
print(keyword.kwlist) #this command print all the keywords supported by puthon 3.x