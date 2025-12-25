# __init__ -> initialization method-> create a constructor

class a:
    def __init__(self, type_, size): #--> why type_? -> as 'type' is a reserved keyword in Python
        self.type = type_
        self.s = size  # instance variable

    def describe(self):
        return f"A {self.type} {self.s} size"
    
order = a("cup", 150)  #-> object with type and size
print(order.describe())  #-> instance method calling via the object 

