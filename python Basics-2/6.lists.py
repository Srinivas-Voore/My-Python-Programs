#List

l=[]
print(l)

l=['srinivas','jithu','navanith']
print(l)

l=[['sai','kiran'],['jithu','katta']]
print(l)

l=[1,'srinu','A',2.98,3+5j]
print(l)


#append(),insert(),extend()

l=[]
l.append(1)
l.append(2)
print(l)

l.insert(3,12)
l.insert(0,'srinu')
print(l)

print(l[2])

l.extend([7,8,9])
print(l)


#[],-ve indexing
l=[]
l=[1,2,3,4,5,6]
print(l[0],l[1],l[2])
print(l[-1],l[-2])


#removing elements remove(),pop()

l=[]
l=[1,2,3,4,5,6,7,8,9,10]
l.remove(1)
l.remove(7)
print(l)

l.pop()
print(l)

del l[0]
print(l)


#slicing

l=[]
l=[1,2,3,4,5]
print(l[1:3:1])

