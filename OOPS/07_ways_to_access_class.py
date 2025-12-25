class a:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength

# class b:
#     def __init__(self, type_, strength, size):
#         self.type = type_
#         self.strength = strength
#         self.size = size

# class b(a):
#     def __init__(self, type_, strength, size):
#         a.__init__(self, type_, strength) #-> explicit call
#         self.size = size

class b(a):
    def __init__(self, type_, strength, size):
        super().__init__(type_, strength)
        self.size = size