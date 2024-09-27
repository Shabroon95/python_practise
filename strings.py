str1='shabroon'
str2="shabroon"

print(id(str1), id(str2))

#strings are immutable
str1='ansar'
print(id(str1))
print(str1)
str1= str1+"welcome"
print(id(str1))
print(str1 *2)
str='Hello world'

print(str[:5])
print(str[4:])
print(str[-10])

print(ord('A'))
print(ord('z'))
print(chr(65))
print(len(str))
print(max('abc'))
print(min('abc'))
print('Hello' in str)
print('world' not in str)

S = 'PYTHON'
c= len(S)
#c=0
for i in S:
    print(i)

#string reverse
for i in S:
    c = c-1
    print(S[c])

i=c
while i<c:
    print(S[c])
    c=c-1

s='welcome to python'

print(s.isalnum())
print("Welcome".isalpha())
print("2012".isdigit())
print("first number".isidentifier())
print(s.lower())
print("WELCOME".isupper())
print(" ".isspace())
print(s.swapcase())
print(s.capitalize())
print(s.title())
print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.replace("python", "C"))



