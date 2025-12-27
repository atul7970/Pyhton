import asyncio
import threading
import time

def background_worker():
    while True:
        time.sleep(1)
        print("Background worker is running...")
        
async def fetch_data():
    await asyncio.sleep(3)  # Simulating an I/O-bound operation
    print("Data fetched.")
    return "Sample Data"

t1 = threading.Thread(target=background_worker, daemon=True) #daemon thread will exit when main program exits
t1.start()

asyncio.run(fetch_data())