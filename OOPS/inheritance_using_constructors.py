class Parent:
    def __init__(self):
        print("This is parent constructor")

class Child(Parent): #Child inherits from both the parents
    def __init__(self):
        print("This is child constructor...")

c = Child()
