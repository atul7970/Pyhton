from multiprocessing import Process, Queue
import time

def cpu_heavy_task(queue):
    queue.put("Starting CPU-heavy task...")


if __name__ == "__main__":
    queue = Queue()
    p=Process(target=cpu_heavy_task, args=(queue,))
    p.start()
    message = queue.get()
    p.join() # Simulate a delay for the CPU-heavy task
    print(message)
