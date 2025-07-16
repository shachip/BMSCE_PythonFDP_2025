#multiple inheritance
class Dad:
    def sleep(self):
        print("sleep..")

class Mom():
    def cook(self):
        print("cook..")

class Child(Dad, Mom): #Child inherits from both the parents
    def study(self):
        print("study...")

d = Dad()
m = Mom()
c = Child()

d.sleep()

m.cook()

c.sleep()
c.cook()
c.study()