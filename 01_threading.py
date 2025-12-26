import threading
import time

def take_orders():
    for i in range(1,4):
        print(f"Taking order {i}")
        time.sleep(2)  # Simulate time taken to take an order

def prepare_food():
    for i in range(1,4):
        print(f"Preparing food for order {i}")
        time.sleep(3)  # Simulate time taken to prepare food

# Create threads for taking orders and preparing food
order_thread = threading.Thread(target=take_orders)
food_thread = threading.Thread(target=prepare_food)

# Start the threads
order_thread.start()
food_thread.start()

# Wait for both threads to complete
order_thread.join()
food_thread.join()

print("All orders taken and food prepared.")


