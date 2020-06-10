#control flow or loops
'''
#while loop
i=0;
while(i<3):
    i+=1;#i=i+1
    print(i)
'''
a=[1,2,3,4,5];

while a:
    print(a.pop());

#while-else

i=10
while i<12:
    print(i,end=" ");
    i+=1;
else:
    print('does execute');


#for loop

l=[1,2,3,4,5]
for i in l:
    print(i);

s='jithu';
for i in s:
    print(i)

#for else loop

for i in s:
    print(i,end="")
else:
    print()
    print("executed else because there is no break in for loop")


#range(start,end-1,stop)

for i in range(5):
    print(i,end=" ")
print()
for i in range(2,9):
    print(i,end=" ")
print()
for i in range(15,30,3):
    print(i,end=" ")
print()
print()

#backward iteration

n=10;
for i in reversed(range(n+1)):
    print(i)
print()
print()
for i in range(n,-1,-1):
    print(i,end=" ");

s='srinivas';
for i in reversed(range(len(s))):
    print(s[i],end=' ');



#loop controllers break,continue,pass
s='srinivas'
for i in s:
    if i=='i':
        break
    print(i,end="")
print()

for i in s:
    if i=='i':
        continue
    print(i,end="")
print()

for i in s:
    if i=='i':
        pass
    print(i,end="")
print()





