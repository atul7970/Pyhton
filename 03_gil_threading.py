import threading
import time

def take_order():
    print(f"{threading.current_thread().name} started taking an order.")
    count = 0
    for _ in range(10000000):
        count += 1  # Simulate some CPU-bound work
    print(f"{threading.current_thread().name} completed taking an order.")

thread1 = threading.Thread(target=take_order, name="Thread-1")
thread2 = threading.Thread(target=take_order, name="Thread-2")

start = time.time()
thread1.start()
thread2.start()

thread1.join()
thread2.join()
end = time.time()

print(f"Both threads completed in {end - start:.4f} seconds.")