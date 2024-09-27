friends={'Tom':'11-22-33', 'Jerry':'22-33-55'}
print(friends)

print(friends['Tom'])

friends['bob']='88-99-77'
print(friends)

friends['Tom']='11-22-44'
print(friends)

del friends['bob']
print(friends)

values= {'a':'100','b':'200', 'c':'300','d':'400'}

for k in values:
    print(k, ":", values[k])

print(len(values))

print(values.pop('a'))
print(values)

d1= {'mike':41, "bob":35}
d2={'bob':35, 'mike':41 }

print(d1==d2)
print(d1!=d2)

print(friends.popitem())
print(friends)
#friends.clear()
#print(friends)
print(friends.keys())
print(values.values())
print(values.get('a'))

dict1={'shab':100000, "Ans":150000, 'Khadar':200000}
print(dict1)

for k in dict1:
    print(k, ':', dict1[k], end=' ')

dict1['shabeena']=60000
print(dict1)

dict1.pop('Khadar')
print(dict1)
print(dict1.values())
print(dict1.keys())
print(dict1.items())
print(dict1.get('shabeena'))

