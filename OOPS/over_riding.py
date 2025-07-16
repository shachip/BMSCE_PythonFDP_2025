#over-riding
class Mom:
    def cook(self):
        print("Indian")

class Daughter(Mom):
    def cook(self): #over-riding - inherit and change
        print("Chinese")

m = Mom()
d = Daughter()

m.cook()
d.cook()
