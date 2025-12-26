import threading
import time


def boil_milk():
    print("Boiling milk...")
    time.sleep(2)  # Simulate time taken to boil milk
    print("Milk is boiled.")

def make_tea():
    print("Making tea...")
    time.sleep(3)  # Simulate time taken to make tea
    print("Tea is ready.")

start = time.time()

milk_thread = threading.Thread(target=boil_milk)
tea_thread = threading.Thread(target=make_tea)

milk_thread.start()
tea_thread.start()


milk_thread.join()
tea_thread.join()

end = time.time()

print(f"Total time taken: {end - start:.2f} seconds")