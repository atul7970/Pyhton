from multiprocessing import Process
import time


def crunch_numbers():
    print(f"Process {Process().name} started crunching numbers.")
    count = 0
    for _ in range(10000000):
        count += 1  # Simulate some CPU-bound work
    print(f"Process {Process().name} completed crunching numbers.")

if __name__ == '__main__':
    process1 = Process(target=crunch_numbers, name="Process-1")
    process2 = Process(target=crunch_numbers, name="Process-2")

    start = time.time()
    process1.start()
    process2.start()

    process1.join()
    process2.join()
    end = time.time()

    print(f"Both processes completed in {end - start:.4f} seconds.")

