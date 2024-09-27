def sum(*args):
    s=0
    for i in args:
        s=s+i   #s+=i
    print(s)


sum(10,20,30,40,50)

def mu_three(a,b,c,d):
    print(a,b,c,d)

args=[1,2,3,4]
mu_three(*args)

def my_threee(a,b,c):
    print(a,b,c)

kwargs={'a':1, 'b':20,'c':50}
my_threee(**kwargs)

def my_func(**kwargs):
    for i,j in kwargs.items():
        print(i,j)

my_func(name='tom', sport='foodball', roll=10)