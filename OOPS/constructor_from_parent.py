#use constructor from parent
class Parent:
    def __init__(self):
        print("This is parent constructor")

class Child(Parent): #Child inherits from both the parents
    def __init__(self):
        super().__init__()#this line calls parent constructor
        print("This is child constructor...")

c = Child()
