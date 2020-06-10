class Person:
    def __init__(self,name):
        self.name=name
    def talk(self):
        print(f"hii, i am {self.name}")



x=Person("srinivas")
print(x.name)
x.talk()

#constructor is always __init__
#self is first parameter of every method


y=Person("krishanth")
print(y.name)
y.talk()
