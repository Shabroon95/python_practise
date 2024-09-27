x=list()
print(x)

list2=list([22,31,53])
print(list2)
list3=list(["toy", "jorry", "spykes", 20,30])
print(list3)

list4= list("python")
print(list4)
print(22 in list2)
print(55 not in list2)
print(len(list4))
print(max(list2))
print(min(list2))
print(sum(list2))


print(list2[0:3])
print(list2[:3])
print(list2[1:])

print(list2+list4)
print(list4*2)
z=[1,2,3,4,5]
for i in z:
    print(i, end=' ')

z.append(6)
print(z)
c=z.count(2)
print(c)
z.extend(list4)
print(z)
z.reverse()
print(list2.index(31))
list2.insert(1, 35)
print(list2)
list2.pop(2)
print(list2.pop(2))
print(list2)
print(z)
z.remove(5)
print(z)
z.reverse()
print(z)
list=[5,7,6,2,4,0,10]
list.sort()
print(list)

list1=[x for x in range(10)]
print(list1)
list1=[x for x in range(1,10,2)]
print(list1)
list2=[x for x in range(0,10,2)]
print(list2)
list3=[x for x in range(10) if x%2==0]
print(list3)


