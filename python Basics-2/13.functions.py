#functions

def f1():
    print('statement 1')

def f2():
    a=0;
    for i in range(1,11):
        a+=i
    return a

f1()
print(f2())


#arguments
#1.default
#2.keyword
#3.variable length

#1.
def f3(x,y=50):
    print("x:",x)
    print("y:",y)

f3(10,20)
f3(15)

#2.
def f4(y,x):
    print(x,y)
f4(x=1,y=2);
f4(y=1,x=2);


#3.


def fx(*a):
    for  i in a:
        print(i)

fx(1,2,3,4,5,6,7,8,9,10)


def fy(**a):
    for i,j in a.items():
        print(f"{i} {j}");

fy(A='a',B='b')


#lambda functions


z=lambda x,y,z:x*y*z
print(z(2,2,2))


'''
def f(x):
    print(1);
    return x*x*x;
    
f(2)

def f(x,y):
    return x*y;
f(2,2)
'''










