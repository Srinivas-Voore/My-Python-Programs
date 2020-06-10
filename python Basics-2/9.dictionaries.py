#dictionaries

d={}
print(d)
d={1:'srinu',2:'jithu'}
print(d)

d={1:"A",2:"B",3:{1:"c",2:"d"}}
print(d)

#adding
d={}
d["nani"]='a';
d["samanta"]='b';
print(d)

#updating
d["nani"]="dobbey";
print(d)

#accessing (keyname),(get() method)

d={1:"A",2:"B"}
print(d[1])
print(d.get(2))

#removing pop(),popitem()

d={1:"A",2:"A",3:"C"}

d.pop(2)
print(d)

d.popitem()
print(d)




