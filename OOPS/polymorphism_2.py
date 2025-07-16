class calc:
    '''def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c'''
    def add(self,a,b):
        return a+b

    def add(self,a,b,c):
        return a+b+c

obj = calc()
#obj.add(1,2)
obj.add(1,2,3)
