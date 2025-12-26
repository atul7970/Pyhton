import threading
import time


def prepare_pizza(type_, wait_time):
    print(f"Preparing {type_} pizza dough...")
    time.sleep(wait_time)  # Simulate time taken to prepare pizza dough
    print(f"{type_} pizza dough is ready.")

#Imp point how to pass arguments to thread function
t1 = threading.Thread(target=prepare_pizza, args=("Margherita", 2))
t2 = threading.Thread(target=prepare_pizza, args=("Pepperoni", 3)) 

t1.start()
t2.start()

t1.join()
t2.join()

print("Both pizzas are ready!")
