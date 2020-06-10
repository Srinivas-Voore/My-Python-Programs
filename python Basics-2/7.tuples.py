#Tuples

t=()
print(t)

t=(1,2)
print(t)

l=[1,2,3,4]

print(l)

t=tuple(l)

print(t)

t1=(1,2,3)
t2=(4,5)
t3=(t1,t2)

print(t3)

#accessing [],-ve indexing

t1=tuple([1,2,3,4])
t2=(1,2,3,4)
print(t1)
print(t2)

print(t[0],t[1],t[-1])


#deletion and updation

del t1

#slicing
t1=(1,2,3,4,5)
print(t[1:3:1])

#unpacking

tx=tuple([1,2,3])

a,b,c=tx
print(a+b+c)


