import asyncio
import time

from concurrent.futures import ThreadPoolExecutor

def check_stock(item):
    print(f"Checking stock for {item}...")
    time.sleep(2)  # Blocking call simulation
    stock = 10  # Simulated stock value
    print(f"Stock for {item}: {stock}")
    return stock

async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result =await loop.run_in_executor(pool, check_stock, "Widget A")
        print(f"Result received: {result}")

asyncio.run(main())