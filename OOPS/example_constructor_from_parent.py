#use constructor from parent
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, usn, name, age): #here 'name' and 'age' comes from the person
        super().__init__(name, age)#this line calls parent constructor
        self.usn = usn

s = Student("1BM21EC123", "Shachi", 20)
print(f"USN:{s.usn} AGE:{s.age} NAME:{s.name}")
