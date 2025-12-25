class a: # class with class methods
    def __init__(self,b,c,d):
        self.b = b
        self.c = c
        self.d = d

    @classmethod  #class method to create object from dictionary
    def from_dict(cls, info):
        return cls(info['b'], info['c'], info['d'])
    
    @classmethod #class method to create object from string
    def from_string(cls, info_str):
        b, c, d = info_str.split("-")
        return cls(b, int(c), float(d))

class b: # class with static method
    @staticmethod
    def is_valid(size): # static method to validate size
        return size in ['small', 'medium', 'large']
    
print(b.is_valid('medium'))  # True
print(b.is_valid('extra large'))  # False


order = a.from_dict({'b': 'item1', 'c': 10, 'd': 20.5})
print(order.__dict__)
print(order.b, order.c, order.d)   

order2 = a.from_string("item2-15-30.75")
print(order2.b, order2.c, order2.d) 
