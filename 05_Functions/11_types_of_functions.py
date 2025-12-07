#pure function
#recommended

def pure_chai(cups):
    return cups * 10

total_chai = 0


#not pure function
#not recommended
def impure_chai(cups):
    global total_chai
    total_chai += cups * 10
    return total_chai
print("Pure function calls:")
print("Order 1:", pure_chai(2))

print(impure_chai(2))
print(impure_chai(3))

def pour_chai(n):
    if n == 0:
        return "Empty cup"
    return pour_chai(n-1)

print(pour_chai(5))


#lamda function

chai_list =["Masala", "Ginger", "Elaichi", "Kesar"]

strong_chai =list(filter(lambda chai: chai!="Kesar", chai_list))

print(strong_chai)