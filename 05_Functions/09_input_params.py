def make_chai(tea, milk, sugar):
    print(f"Making {tea} chai with {milk} milk and {sugar} sugar.")

make_chai("Masala", "full-fat", "2 spoons") #positional arguments
make_chai(tea="Ginger", milk="low-fat", sugar="1 spoon") #keyword arguments




def special_chai(*ingredients, **extras):
    print("Ingredients added.", ingredients)
    print("Extras added.", extras)
special_chai("Masala", "Ginger", "Cardamom", milk="full-fat", sugar="2 spoons", honey="1 tsp")


def chai_order(order=[]):
    order.append("Masala Chai")
    print("Current order:", order)
chai_order()
chai_order()