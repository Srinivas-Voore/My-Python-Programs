#classes and their objects

class Dog:
    dm1='manishi'
    dm2='jentuvu'

    def mf(self):
        print("sai is a",self.dm1);
        print("jithu is a",self.dm2);

z=Dog()
print(z.dm1)
z.mf()

#constructors and destructors
#constructors(__init__()=>constructor)

class addition:
    def __init__(self,a,b):
        self.c=a;
        self.d=b;
    def sum(self):
        print(self.c+self.d);



obj=addition(10,20)
obj.sum();

#destructors(__del__()=>destructor)

class Student:
    def __init__(self):
        print("X");
    def __del__(self):
        print("Y");
obj=Student()
del obj

#inheritance

class person():
    def __init__(self,name):
        self.name=name;
    def getName(self):
        return self.name;
    def isEmployee(self):
        return False;
class employee(person):
    def isEmployee(self):
        return True;

a=person("jithu")
print(a.getName(),a.isEmployee())

b=employee("sai")
print(b.getName(),b.isEmployee())


#polymorphism

class A():
    def add(self):
        print(10+10);

class B():
    def add(self):
        print(10+20);
        
a=A()
a.add()
b=B()
b.add()

'''
#Encapsulation (__=>private,_=>protected)

class Base:
    def __init__(self):
        self._a='jithu'
        self.__b="sai"
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print(self._a,self.__b);
x=Derived()
print(x.a,x.b);

y=Base()
print(y._a,y.__b);
'''
