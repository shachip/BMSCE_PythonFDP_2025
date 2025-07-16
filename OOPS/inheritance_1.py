#single-level
class Animal:
    def eat(self):
        print("Eating..")

class Dog(Animal):
    def bark(self):
        print("Barking..")

a = Animal()
d = Dog()
a.eat()
d.bark()
d.eat()

