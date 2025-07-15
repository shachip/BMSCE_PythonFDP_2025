#to prove that constructor will be created in the backend though not created
class Demo:
    def __init__(self):
        print("I'm a constructor")

d = Demo() #as the object is created, the constructor will be called

