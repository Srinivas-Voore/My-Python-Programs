#mechanism for reusing code
#using parent class in other child classes
'''never duplicate code just try to reduce by using other ways
since if we want to change one thing we must change
it in all the places we used do far and it is a long process'''
#pass means saying nothing just pass on to interpreter
#walk method is inherited in dog and cat class


class Animals:
    def walk(self):
        print("walk")


class Dog(Animals):
    def bark(self):
        print("bark")

class Cat(Animals):
    pass


dog1=Dog()
dog1.walk()
dog1.bark()

cat1=Cat()
cat1.walk()
