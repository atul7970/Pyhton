class Base:
    def __init__(self, type_): #constructor
        self.type = type_

    def display(self):
        print(f"Base type: {self.type}") #constructor variable doen't tobe created here
    
class Derived(Base):  #inheritance
    def add(self):
        print("Adding")#new instance variable for derived class

class a:
    b = Base

    def __init__(self):
        self.d = self.b("Regular")  #creating object of Base class inside a class
    
    def s(self):
        print(f"Hello {self.d.type}") #calling method of Base class using its object
        self.d.display()


class f(a) :  #inheritance
    b = Derived


shop = a()  #object of class a
shop.s()  #calling method of class a which in turn calls method of Base class

g = f()  #object of derived class f
g.s()  #calling method of base class a using derived class object
g.d.add()  #calling method of derived class 
