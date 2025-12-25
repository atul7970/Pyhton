#Calling method inside the class with instance
class a:
    s=150

    def describe(self):
        return f"A{ self.s} size"
    
cup = a()  #-> object

print(cup.describe())  #-> instance method calling via the object

print(a.describe(cup))  #-> class method called with instance