import operations


sum=operations.add(10,20)
mul=operations.mul(10,10)
print(mul,sum)

#approach 2
from operations import add, mul

sum=add(100,200)
mul=mul(10,100)
print(sum,mul)

#approach 3
from operations import *
sum=add(10,20)
mul=mul(5,5)
print(sum,mul)