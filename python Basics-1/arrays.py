import array as ar
a=ar.array('i',[1,2,3,4])

for i in a:
    print(i)

b=ar.array('u',['s','v','n'])

for i in b:
    print(i)

c=ar.array('i',[1,2,3,4])
d=ar.array(c.typecode,(a*3 for a in c))
for i in d:
    print(i,end=' ')

print("\n")
print(len(a))
print(len(d))


for i in range(0,len(a),1):
    print(a[i],end=' ')

print('\n')

for i in range(0,len(d),1):
    print(d[i],end=' ')

print(a[0:4:1])
print(a[:4])
print(a[0:])
print(a[-2:])
print(a[:-1])
print(a[-4:-2])


a[1:3]=ar.array('i',[10,20])
for i in range(0,len(a),1):
    print(a[i])


print(a.typecode)
print(a.itemsize)

g=ar.array('f',[1.0,2.0,3.0])
print(g.itemsize)

