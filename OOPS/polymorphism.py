#not exactly polymorphism
class India:
    def capital(self):
        print("New Delhi")

class USA:
    def capital(self):
        print("Washington DC")

a=India()
b=USA()

print(a.capital) #here capital function has two different roles depending upon the class
print(b.capital)
