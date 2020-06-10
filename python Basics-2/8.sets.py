#sets

s1=set()
s2={}
s3=set([1,2,3,4])
s4={1,2,3,4}


print(s1)
print(s2)
print(s3)
print(s4)


#adding add(),update()

s1=set()
s1.add(1)
s1.add((2,3))
s1.add(1)
print(s1)

s1.update([11,12])
print(s1)

#accessing

s1=set([1,2,3])

for i in s1:
    print(i,end=" ")

print()
#removing remove(),discard(),poop(),clear()

sx=set([1,2,3,4,5,6])
sx.remove(5)
print(sx)
sx.discard(2)
print(sx)
sx.pop()
print(sx)
sx.pop()
print(sx)



#frozen set a set which is immutable
sy={1,2,3,4,5,1,2,3,4,5}
fs=frozenset(sy)
print(fs)

sy.add(10)
print(sy)

sy.add(6)
print(sy)
