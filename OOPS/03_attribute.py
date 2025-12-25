#Attribute Shadowing in Python
class c:
    temperature = 25
    strength = "strong"

obj = c()
print(obj.temperature)


obj.temperature = 30
print(obj.temperature)

obj.d = "new attribute"
print(obj.d)

del obj.temperature
del obj.d

print(obj.temperature)
print(obj.d)  # This will raise an AttributeError since 'd' has been deleted
