#with attributes
class student:
    def __init__(self,name1,usn1): #list the attributes here
        self.name = name1
        self.usn = usn1

    def printDetails(self): #method
        print(f"Name is {self.name}") #self helps in type-safety

s1 = student("Ashank",123)
print(s1.name)
s1.printDetails()

