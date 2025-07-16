#inheritance
class Animal:
    def eat(self):
        print("Eating..")

class Dog(Animal):
    def bark(self):
        print("Barking..")

class Cat(Animal):
    def meow(self):
        print("Meow..")

a = Animal()
d = Dog()
c = Cat()


a.eat()

d.bark()
d.eat()

c.meow()
c.eat()


