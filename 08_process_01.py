from multiprocessing import Process
import time

def cpu_heavy_task():
    print("Starting CPU-heavy task...")
    count = 0
    for i in range(10**9):
        count += i
    print("CPU-heavy task completed.")


if __name__ == "__main__": 
    start_time = time.time()
    
    process = Process(target=cpu_heavy_task)
    process.start()
    process.join()
    
    end_time = time.time()
    print(f"Total time taken: {end_time - start_time} seconds")