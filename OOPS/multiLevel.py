#multi-level
class Animal:
    def eat(self):
        print("Eating..")

class Dog(Animal):
    def bark(self):
        print("Barking..")

class Puppy(Dog): #Animal is the grandparent of Puppy
    def cry(self):
        print("Crying...")


a = Animal()
d = Dog()
p = Puppy()

a.eat()

d.bark()
d.eat()

p.cry()
p.bark()
p.eat()

