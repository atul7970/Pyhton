from multiprocessing import Process, Value

def increment_value(counter):
    for _ in range(100000):
        with counter.get_lock():  # Ensure atomic access to the shared value
            counter.value += 1

if __name__ == "__main__":
    counter = Value('i', 0)  # 'i' indicates a signed integer
    processes = [Process(target=increment_value, args=(counter,)) for _ in range(4)]  # Create 4 processes
    [p.start() for p in processes]
    [p.join() for p in processes]
    print(f"Final counter value: {counter.value}")

