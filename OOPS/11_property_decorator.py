class Leaf:
    def __init__(self, color):
        self._color = color  # private variable

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, value): # setter method
        self._color = value

leaf = Leaf("Green")
print(leaf.color)  # accessing property

leaf.color = "Yellow"  # modifying property
print(leaf.color)  # accessing modified property        

# Output:
# Green 
# Yellow